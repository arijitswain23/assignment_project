<template>
  <button class="base-button" :type="type" @click="$emit('click')">
    <slot />
  </button>
</template>

<script setup>
defineProps({ type: { type: String, default: 'button' } })
</script>

<style scoped>
.base-button {
  background: #1976d2;
  color: #fff;
  border: none;
  padding: 0.8rem;
  border-radius: 6px;
  font-size: 1rem;
  cursor: pointer;
  width: 100%;
  margin-top: 0.5rem;
  transition: background 0.2s;
}
.base-button:hover {
  background: #1565c0;
}
</style>
