<template>
  <div class="full-bg">
    <div class="dashboard-overlay">
      <div class="dashboard-content" v-if="user">
        <h2>Welcome, {{ user.full_name }}!</h2>
        <div class="details">
          <p><strong>Username:</strong> {{ user.username }}</p>
          <p><strong>Email:</strong> {{ user.email }}</p>
          <p><strong>Full Name:</strong> {{ user.full_name || 'N/A' }}</p>
          <p><strong>Role:</strong> 
            <span v-if="user.is_superuser">Superuser</span>
            <span v-else-if="user.is_staff">Staff</span>
            <span v-else>User</span>
          </p>
        </div>
        <button @click="logout">Logout</button>
      </div>
      <div v-else class="loading">Loading...</div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from '../axios'
import { useRouter } from 'vue-router'

const user = ref(null)
const router = useRouter()

onMounted(async () => {
  try {
    const res = await axios.get('dashboard/')
    user.value = res.data
  } catch {
    router.push('/login')
  }
})

const logout = async () => {
  await axios.post('logout/')
  router.push('/login')
}
</script>

<style scoped>
.full-bg {
  min-height: 100vh;
  min-width: 100vw;
  background: url('https://img.freepik.com/premium-vector/abstract-modern-background_8221-611.jpg?semt=ais_hybrid&w=740') no-repeat center center / cover;
  display: flex;
  align-items: center;
  justify-content: center;
}

.dashboard-overlay {
  background: rgba(255, 255, 255, 0.85);
  padding: 2rem;
  border-radius: 18px;
  box-shadow: 0 4px 32px rgba(0, 0, 0, 0.1);
  width: 90%;
  max-width: 500px;
  text-align: center;
}

.dashboard-content h2 {
  color: #1976d2;
  margin-bottom: 1rem;
}

.details p {
  margin: 0.5rem 0;
  font-size: 1rem;
  color: #333;
}

.dashboard-content button {
  margin-top: 1.5rem;
  background: #1976d2;
  color: #fff;
  border: none;
  padding: 0.8rem 2rem;
  border-radius: 6px;
  font-size: 1rem;
  cursor: pointer;
  transition: background 0.2s;
}

.dashboard-content button:hover {
  background: #1565c0;
}

.loading {
  color: #1976d2;
  font-size: 1.2rem;
}

@media (max-width: 500px) {
  .dashboard-overlay {
    padding: 1rem;
  }
}
</style>
