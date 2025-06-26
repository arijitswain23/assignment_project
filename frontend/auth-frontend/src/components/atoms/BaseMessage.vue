<template>
  <div :class="['base-message', type]">
    <slot />
  </div>
</template>

<script setup>
defineProps({ type: { type: String, default: 'info' } })
</script>

<style scoped>
.base-message {
  text-align: center;
  margin-top: 0.5rem;
  padding: 0.5rem;
  border-radius: 4px;
  font-size: 0.98rem;
}
.base-message.info { color: #1976d2; background: #e3f2fd; }
.base-message.success { color: #388e3c; background: #e8f5e9; }
.base-message.error { color: #d32f2f; background: #ffebee; }
</style>
