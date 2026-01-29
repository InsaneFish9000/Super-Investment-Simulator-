<template>
  <div class="dashboard-wrapper">
    <header class="dashboard-header">
      <div>
        <h1>Investment Overview</h1>
        <p class="date-display">{{ currentDate }}</p>
      </div>
      <button class="refresh-btn" @click="refreshData">↻ Refresh Data</button>
    </header>

    <section class="stats-grid">
      <div class="stat-card">
        <span class="stat-label">Total Portfolio Value</span>
        <div class="stat-value">$24,500.00</div>
        <span class="stat-change positive">▲ 4.2% (Past 30d)</span>
      </div>
      <div class="stat-card">
        <span class="stat-label">Total Invested</span>
        <div class="stat-value">$20,000.00</div>
      </div>
      <div class="stat-card">
        <span class="stat-label">Overall Profit</span>
        <div class="stat-value profit">+$4,500.00</div>
      </div>
    </section>

    <div class="content-grid">
      <section class="asset-section card">
        <h3>Current Holdings</h3>
        <table class="asset-table">
          <thead>
            <tr>
              <th>Asset</th>
              <th>Price</th>
              <th>Holdings</th>
              <th>Total</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="asset in assets" :key="asset.id">
              <td><strong>{{ asset.symbol }}</strong></td>
              <td>${{ asset.price }}</td>
              <td>{{ asset.units }}</td>
              <td>${{ (asset.price * asset.units).toFixed(2) }}</td>
            </tr>
          </tbody>
        </table>
      </section>

      <section class="tool-section">
        <LumpSumCalculator />
      </section>
    </div>
  </div>
</template>

<script setup>
import LumpSumCalculator from './LumpSumCalculator.vue'
import { ref } from 'vue';

const currentDate = new Date().toLocaleDateString('en-US', { 
  weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' 
});

const assets = ref([
  { id: 1, symbol: 'BTC', price: 45000, units: 0.2 },
  { id: 2, symbol: 'ETH', price: 2400, units: 2.5 },
  { id: 3, symbol: 'VOO', price: 480, units: 15 },
]);

const refreshData = () => {
  console.log("Fetching latest prices from FastAPI...");
};
</script>

<style scoped>
.dashboard-wrapper {
  padding: 2rem;
  max-width: 1200px;
  margin: 0 auto;
  color: #2d3748;
}

.dashboard-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 2rem;
}

.date-display { color: #718096; margin-top: 4px; }

.refresh-btn {
  padding: 8px 16px;
  background: white;
  border: 1px solid #cbd5e0;
  border-radius: 6px;
  cursor: pointer;
  transition: all 0.2s;
}

.refresh-btn:hover {
  background: #f7fafc;
  border-color: #a0aec0;
}

/* Stats Cards */
.stats-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 1.5rem;
  margin-bottom: 2rem;
}

.stat-card {
  background: white;
  padding: 1.5rem;
  border-radius: 12px;
  box-shadow: 0 2px 10px rgba(0,0,0,0.05);
  border: 1px solid #eef2f6;
}

.stat-label { font-size: 0.85rem; color: #718096; text-transform: uppercase; }
.stat-value { font-size: 1.8rem; font-weight: bold; margin: 8px 0; }
.profit { color: #38a169; }
.positive { color: #38a169; font-size: 0.85rem; font-weight: bold; }

/* Main Grid */
.content-grid {
  display: grid;
  grid-template-columns: 2fr 1fr;
  gap: 1.5rem;
}

/* Responsive fix for smaller screens */
@media (max-width: 900px) {
  .content-grid {
    grid-template-columns: 1fr;
  }
}

.card {
  background: white;
  padding: 1.5rem;
  border-radius: 12px;
  box-shadow: 0 2px 10px rgba(0,0,0,0.05);
}

.asset-table {
  width: 100%;
  border-collapse: collapse;
  margin-top: 1rem;
}

.asset-table th {
  text-align: left;
  padding: 12px;
  border-bottom: 2px solid #edf2f7;
  color: #718096;
  font-size: 0.85rem;
}

.asset-table td {
  padding: 12px;
  border-bottom: 1px solid #edf2f7;
}
</style>