<template>
  <div class="full-bg">
    <div class="center-card">
      <div class="img-col">
        <img src="https://static.vecteezy.com/system/resources/previews/027/205/841/non_2x/login-and-password-concept-3d-illustration-computer-and-account-login-and-password-form-page-on-screen-3d-illustration-png.png" alt="Login" class="side-img" />
      </div>
      <form class="auth-form" @submit.prevent="login">
        <h2>Log In</h2>
        <input v-model="username" placeholder="Username" required />
        <div v-if="errors.username" class="field-error">{{ errors.username }}</div>
        <input v-model="password" type="password" placeholder="Password" required />
        <div v-if="errors.password" class="field-error">{{ errors.password }}</div>
        <button type="submit">Login</button>
        <p class="switch-link">
          Don't have an account?
          <router-link to="/register">Register</router-link>
        </p>
        <div v-if="message" class="message" :class="{ error: isError }">{{ message }}</div>
      </form>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import axios from '../axios'
import { useRouter } from 'vue-router'

const username = ref('')
const password = ref('')
const message = ref('')
const isError = ref(false)
const errors = ref({})
const router = useRouter()

const validate = () => {
  errors.value = {}
  if (!username.value.trim()) errors.value.username = 'Username is required'
  if (!password.value) errors.value.password = 'Password is required'
  return Object.keys(errors.value).length === 0
}

const login = async () => {
  isError.value = false
  message.value = ''
  if (!validate()) return
  try {
    await axios.post('login/', {
      username: username.value,
      password: password.value
    })
    const res = await axios.get('dashboard/')
    if (res.data.is_superuser || res.data.is_staff) {
      router.push('/admin-dashboard')
    } else {
      router.push('/dashboard')
    }
  } catch (e) {
    isError.value = true
    message.value = e.response?.data?.message || 'Login failed'
  }
}
</script>

<style scoped>
.full-bg {
  min-height: 100vh;
  min-width: 100vw;
  background: linear-gradient(120deg, #fbc2eb 0%, #a6c1ee 100%);
  display: flex;
  align-items: center;
  justify-content: center;
}
.center-card {
  display: flex;
  background: #fff;
  border-radius: 18px;
  box-shadow: 0 4px 32px rgba(0,0,0,0.10);
  overflow: hidden;
  max-width: 900px;
  width: 100%;
  margin: 2rem;
}
.img-col {
  display: flex;
  align-items: center;
  justify-content: center;
  background: #f3e5f5;
  padding: 2rem;
}
.side-img {
  width: 260px;
  max-width: 100%;
  height: auto;
}
.auth-form {
  flex: 1;
  padding: 2.5rem 2rem;
  display: flex;
  flex-direction: column;
  gap: 1rem;
  min-width: 300px;
  max-width: 400px;
  justify-content: center;
}
.auth-form h2 {
  margin-bottom: 1rem;
  color: #d81b60;
  text-align: center;
}
.auth-form input {
  padding: 0.7rem;
  border: 1px solid #e0e0e0;
  border-radius: 6px;
  font-size: 1rem;
  outline: none;
  transition: border 0.2s;
}
.auth-form input:focus {
  border: 1.5px solid #d81b60;
}
.auth-form button {
  background: #d81b60;
  color: #fff;
  border: none;
  padding: 0.8rem;
  border-radius: 6px;
  font-size: 1rem;
  cursor: pointer;
  transition: background 0.2s;
}
.auth-form button:hover {
  background: #ad1457;
}
.switch-link {
  text-align: center;
  font-size: 0.95rem;
}
.switch-link a {
  color: #d81b60;
  text-decoration: none;
  margin-left: 0.3rem;
}
.message {
  text-align: center;
  margin-top: 0.5rem;
  color: #388e3c;
}
.message.error {
  color: #d32f2f;
}
.field-error {
  color: #d32f2f;
  font-size: 0.95rem;
  margin-bottom: -0.5rem;
  margin-top: -0.5rem;
  text-align: left;
}
button[disabled] {
  opacity: 0.6;
  cursor: not-allowed;
}
@media (max-width: 800px) {
  .center-card {
    flex-direction: column;
    align-items: center;
  }
  .img-col {
    padding: 1rem;
  }
  .side-img {
    width: 180px;
  }
}
@media (max-width: 500px) {
  .center-card {
    margin: 0.5rem;
  }
  .auth-form {
    padding: 1.2rem 0.5rem;
    min-width: 0;
    max-width: 100vw;
  }
}
</style>
  