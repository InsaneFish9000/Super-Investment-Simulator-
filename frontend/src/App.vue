<script setup>
import Dashboard from './components/Dashboard.vue'
</script>

<!-- This is the top dashboard with VUE logo and InvestTrack -->
<template>
  <div class="app-container">
    <nav class="top-nav">
      <div class="logo-area">
        <img alt="Vue logo" class="logo" src="@/assets/logo.svg" width="30" height="30" />
        <span class="brand-name">InvestTrack</span>
      </div>
      <div class="user-profile">
        <span>Demo User</span>
      </div>
    </nav>

    <main>
      <Dashboard />
    </main>
  </div>
</template>

<style>
/* Reset and Global Styles */
body {
  margin: 0;
  padding: 0;
  background-color: #9fe2cc; /* Light grey background for the whole app */
  font-family: 'Inter', sans-serif;
}

.app-container {
  min-height: 100vh;
}

.top-nav {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0.75rem 2rem;
  background-color: #1a202c; /* Dark navy professional feel */
  color: white;
}

.logo-area {
  display: flex;
  align-items: center;
  gap: 10px;
}

.brand-name {
  font-weight: bold;
  font-size: 1.2rem;
  letter-spacing: 0.5px;
}

.user-profile {
  font-size: 0.9rem;
  opacity: 0.8;
}

main {
  padding-top: 1rem;
}
</style>