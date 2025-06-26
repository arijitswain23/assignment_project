<template>
  <div class="approval-list">
    <h3>Pending User Requests</h3>
    <div v-if="users.length === 0" class="empty">
      <img src="https://cdn-icons-png.flaticon.com/512/4076/4076549.png" alt="No requests" class="empty-img" />
      <div>No users to approve.</div>
    </div>
    <div class="user-cards">
      <div v-for="user in users" :key="user.id" class="user-card">
        <div class="user-header">
          <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR56rn6SPM8T2swfi_RHpSe1SWVBUMZDm9kd418KVsDq7RHyksHSEqT6mel1JQ845Erack&usqp=CAU" class="avatar" :alt="user.username" />
          <div>
            <div class="user-name">{{ user.full_name }}</div>
            <div class="user-role">
              <span v-if="user.is_superuser" class="role superuser">Superuser</span>
              <span v-else-if="user.is_staff" class="role staff">Staff</span>
              <span v-else class="role user">User</span>
            </div>
          </div>
        </div>
        <div class="user-details">
          <div><span class="label">Username:</span> {{ user.username }}</div>
          <div><span class="label">Full Name:</span> {{ user.full_name }}</div>
          <div><span class="label">Email:</span> {{ user.email }}</div>
          <div><span class="label">Approved:</span> {{ user.is_approved ? 'Yes' : 'No' }}</div>
        </div>
        <button class="approve-btn" @click="approve(user.id)">Approve</button>
      </div>
    </div>
    <div v-if="message" class="message" :class="messageType">{{ message }}</div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from '@/axios'

const users = ref([])
const message = ref('')
const messageType = ref('info')

const fetchUsers = async () => {
  const res = await axios.get('users/?is_approved=false')
  users.value = res.data
}

const approve = async (userId) => {
  try {
    await axios.post(`approve/${userId}/`)
    message.value = 'User approved!'
    messageType.value = 'success'
    users.value = users.value.filter(u => u.id !== userId)
  } catch {
    message.value = 'Failed to approve user'
    messageType.value = 'error'
  }
}

onMounted(fetchUsers)
</script>

<style scoped>
.approval-list {
  width: 100%;
  margin: 0 auto;
  padding: 1rem 0;
}
.approval-list h3 {
  color: #1976d2;
  margin-bottom: 1.5rem;
  text-align: center;
  font-size: 1.5rem;
  font-weight: 700;
  letter-spacing: 1px;
}
.user-cards {
  display: flex;
  flex-wrap: wrap;
  gap: 1.5rem;
  justify-content: center;
}
.user-card {
  background: rgba(255,255,255,0.95);
  border-radius: 16px;
  box-shadow: 0 4px 24px rgba(25, 118, 210, 0.10);
  padding: 1.5rem 1.2rem;
  min-width: 260px;
  max-width: 320px;
  width: 100%;
  display: flex;
  flex-direction: column;
  align-items: stretch;
  margin-bottom: 1rem;
  transition: box-shadow 0.2s;
  border: 1.5px solid #e3f2fd;
}
.user-card:hover {
  box-shadow: 0 8px 32px rgba(25, 118, 210, 0.18);
}
.user-header {
  display: flex;
  align-items: center;
  gap: 1rem;
  margin-bottom: 1rem;
}
.avatar {
  width: 54px;
  height: 54px;
  border-radius: 50%;
  background: #e3f2fd;
  object-fit: cover;
  border: 2px solid #1976d2;
}
.user-name {
  font-size: 1.2rem;
  font-weight: 600;
  color: #1976d2;
}
.user-role .role {
  font-size: 0.95rem;
  font-weight: 500;
  padding: 0.1rem 0.5rem;
  border-radius: 6px;
  margin-right: 0.3rem;
}
.role.superuser { background: #ffd600; color: #333; }
.role.staff { background: #b2ff59; color: #333; }
.role.user { background: #e3f2fd; color: #1976d2; }
.user-details {
  font-size: 1rem;
  color: #333;
  margin-bottom: 1.2rem;
}
.user-details .label {
  font-weight: 600;
  color: #1976d2;
  margin-right: 0.3rem;
}
.approve-btn {
  background: #1976d2;
  color: #fff;
  border: none;
  padding: 0.7rem 0;
  border-radius: 8px;
  font-size: 1rem;
  font-weight: 600;
  cursor: pointer;
  transition: background 0.2s;
  margin-top: auto;
}
.approve-btn:hover {
  background: #1565c0;
}
.empty {
  text-align: center;
  color: #888;
  margin: 2rem 0;
  display: flex;
  flex-direction: column;
  align-items: center;
}
.empty-img {
  width: 80px;
  margin-bottom: 1rem;
  opacity: 0.7;
}
.message {
  text-align: center;
  margin-top: 1rem;
  font-size: 1.1rem;
  border-radius: 6px;
  padding: 0.5rem 1rem;
}
.message.success { color: #388e3c; background: #e8f5e9; }
.message.error { color: #d32f2f; background: #ffebee; }
@media (max-width: 700px) {
  .user-cards {
    flex-direction: column;
    align-items: center;
  }
  .user-card {
    min-width: 0;
    max-width: 98vw;
  }
}
</style>
