<template>
  <div class="full-bg">
    <div class="center-card">
      <div class="img-col">
        <img src="https://static.vecteezy.com/system/resources/previews/010/925/404/non_2x/registration-page-name-and-password-field-fill-in-form-menu-bar-corporate-website-create-account-user-information-flat-design-modern-illustration-vector.jpg" alt="Register" class="side-img" />
      </div>
      <form class="auth-form" @submit.prevent="register">
        <h2>Register Now</h2>
        <input v-model="username" placeholder="Username" required />
        <div v-if="errors.username" class="field-error">{{ errors.username }}</div>
        <input v-model="email" type="email" placeholder="Email" required />
        <div v-if="errors.email" class="field-error">{{ errors.email }}</div>
        <input v-model="full_name" placeholder="Full Name" required />
        <div v-if="errors.full_name" class="field-error">{{ errors.full_name }}</div>
        <input v-model="password" type="password" placeholder="Password" required />
        <div v-if="errors.password" class="field-error">{{ errors.password }}</div>
        <button type="submit" :disabled="!canSubmit">Register</button>
        <p class="switch-link">
          Already have an account?
          <router-link to="/login">Login</router-link>
        </p>
        <div v-if="message" class="message">{{ message }}</div>
      </form>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import axios from '../axios'
import { useRouter } from 'vue-router'

const username = ref('')
const password = ref('')
const email = ref('')
const full_name = ref('')
const message = ref('')
const errors = ref({})
const router = useRouter()

const validate = () => {
  errors.value = {}
  if (!username.value.trim()) errors.value.username = 'Username is required'
  if (!email.value.trim()) errors.value.email = 'Email is required'
  else if (!/^[\w-.]+@([\w-]+\.)+[\w-]{2,4}$/.test(email.value))
    errors.value.email = 'Invalid email address'
  if (!full_name.value.trim()) errors.value.full_name = 'Full name is required'
  if (!password.value) errors.value.password = 'Password is required'
  else if (password.value.length < 6)
    errors.value.password = 'Password must be at least 6 characters'
  return Object.keys(errors.value).length === 0
}

const canSubmit = computed(() => validate())

const register = async () => {
  if (!validate()) return
  try {
    await axios.post('register/', {
      username: username.value,
      password: password.value,
      email: email.value,
      full_name: full_name.value
    })
    message.value = 'Registered! Wait for admin approval.'
    setTimeout(() => router.push('/login'), 2000)
  } catch (e) {
    message.value = e.response?.data?.message || 'Registration failed'
  }
}
</script>

<style scoped>
.full-bg {
  height: 100vh;
  width: 100vw;
  background: linear-gradient(120deg, #a1c4fd 0%, #c2e9fb 100%);
  display: flex;
  align-items: center;
  justify-content: center;
  overflow-x: hidden;
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
  background: #e3f2fd;
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
  color: #1976d2;
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
  border: 1.5px solid #1976d2;
}
.auth-form button {
  background: #1976d2;
  color: #fff;
  border: none;
  padding: 0.8rem;
  border-radius: 6px;
  font-size: 1rem;
  cursor: pointer;
  transition: background 0.2s;
}
.auth-form button:hover {
  background: #1565c0;
}
.switch-link {
  text-align: center;
  font-size: 0.95rem;
}
.switch-link a {
  color: #1976d2;
  text-decoration: none;
  margin-left: 0.3rem;
}
.message {
  text-align: center;
  color: #388e3c;
  margin-top: 0.5rem;
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
  