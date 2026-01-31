<script setup>
import Dashboard from './components/Dashboard.vue'
</script>

<template>
    <div class="app-container">
        <nav class="top-nav">
            <div class="logo-area">
                <img alt="Vue logo" class="logo" src="@/assets/logo.svg" width="30" height="30" />
                <span class="brand-name">InvestTrack</span>
            </div>
            <div class="user-profile">
                <span class="user-badge">DEMO</span>
            </div>
        </nav>

        <main class="main-content">
            <Dashboard />
        </main>
    </div>
</template>

<style>
/* Reset and Global Styles */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    margin: 0;
    padding: 0;
    background-color: #f0f2f5;
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', 'Oxygen',
        'Ubuntu', 'Cantarell', 'Fira Sans', 'Droid Sans', 'Helvetica Neue',
        sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    color: #1a202c;
    width: 100vw;
    overflow-x: hidden;
}

.app-container {
    min-height: 100vh;
    width: 100%;
    display: flex;
    flex-direction: column;
}

.top-nav {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 0.75rem 0.5rem;
    background: linear-gradient(135deg, #1a202c 0%, #2d3748 100%);
    color: white;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
    position: sticky;
    top: 0;
    z-index: 100;
    backdrop-filter: blur(10px);
    width: 100%;
    margin: 0;
    box-sizing: border-box;
}

.logo-area {
    display: flex;
    align-items: center;
    gap: 0.75rem;
}

.logo {
    width: 30px;
    height: 30px;
    filter: drop-shadow(0 2px 4px rgba(0, 0, 0, 0.2));
}

.brand-name {
    font-weight: 700;
    font-size: 1.25rem;
    letter-spacing: 0.02em;
}

.user-profile {
    font-size: 0.9375rem;
}

.user-badge {
    background: rgba(255, 255, 255, 0.15);
    padding: 0.375rem 0.875rem;
    border-radius: 6px;
    font-weight: 600;
    letter-spacing: 0.05em;
    backdrop-filter: blur(10px);
    border: 1px solid rgba(255, 255, 255, 0.2);
}

.main-content {
    flex: 1;
    width: 100%;
    margin: 0;
    box-sizing: border-box;
}

/* Responsive Typography */
@media (max-width: 768px) {
    .top-nav {
        padding: 0.75rem 1rem;
    }
}

@media (max-width: 480px) {
    .brand-name {
        font-size: 1rem;
    }
    
    .user-badge {
        padding: 0.25rem 0.625rem;
        font-size: 0.75rem;
    }
}
</style>