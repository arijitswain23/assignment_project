<template>
  <form class="auth-form" @submit.prevent="onSubmit">
    <h2>{{ title }}</h2>
    <BaseInput v-model="username" placeholder="Username" autocomplete="username" />
    <BaseInput v-model="password" type="password" placeholder="Password" autocomplete="current-password" />
    <BaseButton type="submit">{{ buttonText }}</BaseButton>
    <BaseMessage v-if="message" :type="messageType">{{ message }}</BaseMessage>
  </form>
</template>

<script setup>
import { ref } from 'vue'
import BaseInput from '../atoms/BaseInput.vue'
import BaseButton from '../atoms/BaseButton.vue'
import BaseMessage from '../atoms/BaseMessage.vue'

const props = defineProps({
  title: String,
  buttonText: String,
  onSubmitForm: Function
})

const username = ref('')
const password = ref('')
const message = ref('')
const messageType = ref('info')

const onSubmit = async () => {
  message.value = ''
  try {
    await props.onSubmitForm(username.value, password.value, message, messageType)
  } catch (e) {
    message.value = 'Something went wrong'
    messageType.value = 'error'
  }
}
</script>

<style scoped>
.auth-form {
  background: #fff;
  padding: 2.5rem 2rem;
  border-radius: 12px;
  box-shadow: 0 4px 32px rgba(0,0,0,0.08);
  width: 100%;
  max-width: 350px;
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}
.auth-form h2 {
  margin-bottom: 1rem;
  color: #1976d2;
  text-align: center;
}
</style>
