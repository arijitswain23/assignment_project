<template>
  <input
    :type="type"
    :placeholder="placeholder"
    :value="modelValue"
    @input="$emit('update:modelValue', $event.target.value)"
    class="base-input"
    :autocomplete="autocomplete"
  />
</template>

<script setup>
defineProps(['modelValue', 'type', 'placeholder', 'autocomplete'])
</script>

<style scoped>
.base-input {
  padding: 0.7rem;
  border: 1px solid #e0e0e0;
  border-radius: 6px;
  font-size: 1rem;
  outline: none;
  width: 100%;
  margin-bottom: 0.5rem;
  transition: border 0.2s;
}
.base-input:focus {
  border: 1.5px solid #1976d2;
}
</style>
