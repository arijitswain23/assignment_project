<template>
  <div class="admin-bg">
    <aside class="sidebar">
      <img src="https://t4.ftcdn.net/jpg/02/27/45/09/360_F_227450952_KQCMShHPOPebUXklULsKsROk5AvN6H1H.jpg" alt="Admin" class="sidebar-img" />
      <h1>Admin Panel</h1>
      <button class="logout-btn" @click="logout">Logout</button>
    </aside>
    <main class="main-content">
      <header class="admin-header">
        <h2>Welcome, Admin!</h2>
        <p>Manage user approvals below.</p>
      </header>
      <section class="approval-section">
        <UserApprovalList />
      </section>
    </main>
  </div>
</template>

<script setup>
import UserApprovalList from '../organisms/UserApprovalList.vue'
import axios from '../axios'
import { useRouter } from 'vue-router'

const router = useRouter()
const logout = async () => {
  await axios.post('logout/')
  router.push('/admin-login')
}
</script>

<style scoped>
.admin-bg {
  display: flex;
  height: 100vh;
  width: 100vw;
  background: linear-gradient(120deg, #fdfbfb 0%, #ebedee 100%);
  overflow-x: hidden;
}
.sidebar {
  background: #1976d2;
  color: #fff;
  width: 260px;
  min-width: 180px;
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 2rem 1rem 1rem 1rem;
  box-shadow: 2px 0 16px rgba(25, 118, 210, 0.08);
  z-index: 2;
}
.sidebar-img {
  width: 100px;
  margin-bottom: 1.5rem;
  border-radius: 12px;
  background: #fff;
  padding: 0.5rem;
}
.sidebar h1 {
  font-size: 1.5rem;
  margin-bottom: 2rem;
  font-weight: 700;
  letter-spacing: 1px;
}
.logout-btn {
  margin-top: auto;
  background: #fff;
  color: #1976d2;
  border: none;
  padding: 0.7rem 1.5rem;
  border-radius: 6px;
  font-size: 1rem;
  cursor: pointer;
  font-weight: 600;
  transition: background 0.2s, color 0.2s;
}
.logout-btn:hover {
  background: #1565c0;
  color: #fff;
}
.main-content {
  flex: 1;
  display: flex;
  flex-direction: column;
  padding: 2.5rem 2rem;
  overflow-y: auto;
}
.admin-header {
  margin-bottom: 2rem;
}
.admin-header h2 {
  color: #1976d2;
  font-size: 2rem;
  margin-bottom: 0.5rem;
}
.admin-header p {
  color: #555;
  font-size: 1.1rem;
}
.approval-section {
  max-width: 700px;
  margin: 0 auto;
  width: 100%;
}
@media (max-width: 900px) {
  .admin-bg {
    flex-direction: column;
  }
  .sidebar {
    flex-direction: row;
    width: 100vw;
    min-width: 0;
    padding: 1rem 0.5rem;
    justify-content: space-between;
    align-items: center;
  }
  .sidebar-img {
    width: 60px;
    margin-bottom: 0;
    margin-right: 1rem;
  }
  .sidebar h1 {
    margin-bottom: 0;
    font-size: 1.1rem;
  }
  .logout-btn {
    margin-top: 0;
    margin-left: 1rem;
  }
  .main-content {
    padding: 1.2rem 0.5rem;
  }
}
@media (max-width: 600px) {
  .admin-header h2 {
    font-size: 1.2rem;
  }
  .approval-section {
    padding: 0;
  }
}
</style>
