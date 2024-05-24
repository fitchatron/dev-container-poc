export async function getHomeRoute() {
  console.log('fetching...')

  const resp = await fetch('/')
  console.log('response is ', resp)
}
