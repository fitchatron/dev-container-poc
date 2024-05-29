# Using Docker for local dev and CI/CD

## Purpose

The aim of this repo is to provide a simple example of how we can use Docker for local development and production builds.

## Summary

In short, the aim is to have a prod and dev `Dockerfile` for both the frontend and the backend. There would also be a base `compose.yml` file, and a prod and dev version. When running in dev, you would run the `compose.dev.yml` which would override the `compose.yml` with the dev parameters / logic. Same for prod. This would allow the dev to spin up their dev env locally, perform dev - possibly with a local DB on an image. When it comes time to deploy, the GitHub Action would override the `compose.yml` with the `compose.prod.yml` file which would perform the prod build.

## Dockerfile

There are two Dockerfiles in each service. One for the prod steps and one for the dev steps. This is useful when the steps involved in local dev vary greatly from prod builds.

An example of this is the frontend. Building for prod broadly speaking, could involve:

- Using the base node image
- Installing pnpm
- Installing packages
- Performing a prod build
- Removing dev dependencies
- Serving for an nginx image

These steps would be overkill for local development though. We wouldn't want to build each time as this could be time consuming as the project grows.

Ideally, the dev process would be:

- Using the base node image
- Installing pnpm
- Installing packages
- Run dev server

Two Dockerfiles allows us to run two very different workflows based on the situation.

Naming could be `Dockerfile` and `Dockerfile.prod`. It's up to us to decide however, `Dockerfile.dev` and `Dockerfile.prod` seems to be the most logical from a readability perspective.

## Compose File

The root of the project has three compose files. The base `compose.yml` file is always overwritten and is just required for compose. The `compose.dev.yml` is used to inject the development compose logic while the `compose.prod.yml` overrides with the prod logic. This approach allows us to define different services and logic for prod and dev. For example, including a local database in the `compose.dev.yml` which isn't present on the `compose.prod.yml`.

We can also specify override `CMD` instructions using the `command` key. This would allow us to utilise one Dockerfile for a service and override the final command for a specific build workflow. The backend would be a good candidate for this.

## Frontend

The frontend has a `Dockerfile` and a `Dockerfile.prod`. The Dockerfile is used for development and installs packages, creates a restricted user and runs the dev environment in a container. The compose file allows us to watch for certain file changes and act accordingly. For example, below is for docker compose watch mode. Anything mentioned under develop will be watched for changes by docker compose watch and it will perform the action mentioned. This uses caching in the Dockerfile to sync file changes (i.e. hot reload) and rebuild where packages are installed (changing package.json).

```yml

develop:
    # we specify the files to watch for changes
    watch:
    # it'll watch for changes in package.json and package-lock.json and rebuild the container if there are any changes
    - path: ./frontend/package.json
        action: rebuild
    - path: ./frontend/package-lock.json
        action: rebuild
    # it'll watch for changes in the frontend directory and sync the changes with the container real time
    - path: ./frontend
        target: /app
        action: sync
```

# Backend

The backend has a `Dockerfile` and a `Dockerfile.prod`. Inspecting both shows that the dev and prod files only differ in the final command. Fastapi allows you to spin up the server using a few similar commands however, one command and thus one `Dockerfile` could be used. Two have been created to illustrate what it could look like. Another solution is providing an override command in the `compose.dev.yml`. Thereby using one `Dockerfile`.

```yml
api:
  #...more
  build:
    context: ./backend
    dockerfile: Dockerfile
  container_name: onboard-api-dev
  command: fastapi dev main.py
#...more
```
