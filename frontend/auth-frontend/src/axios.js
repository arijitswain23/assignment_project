import axios from 'axios'

const instance = axios.create({
  baseURL: 'http://localhost:8000/api/',
  withCredentials: true // Important for session auth
})

export default instance
