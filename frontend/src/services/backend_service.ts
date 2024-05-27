import axios from 'axios'

const headers = {
  'Content-type': 'application/json'
}
const backend_axios = axios.create({
  headers
})

export async function getHomeRoute() {
  console.log('fetching...')
  return fetch('/api/status', { headers })
}

export async function getItemByIdRoute(id: number, query: string = 'james') {
  console.log('fetching...')

  return backend_axios({
    url: `/api/items/${id}${query ? '?q=james' : ''}`,
    method: 'GET'
  })
}
