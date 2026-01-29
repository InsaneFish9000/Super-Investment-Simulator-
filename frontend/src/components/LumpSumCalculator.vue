<template>
  <div class="widget-card">
    <div class="widget-header">
      <h3>Lump Sum Calculator</h3>
      <span class="subtitle">Historical Performance Analysis</span>
    </div>

    <div class="widget-body">
      <div class="input-grid">
        <div class="input-group">
          <label>Start Date</label>
          <input type="date" v-model="startDate" />
        </div>

        <div class="input-group">
          <label>Investment Amount ($)</label>
          <input type="number" v-model="startAmount" placeholder="e.g. 1000" />
        </div>
      </div>

      <button @click="calculateLumpSum" class="calc-button">
        Calculate Returns
      </button>

      <div v-if="error" class="error-banner">
        {{ error }}
      </div>

      <div v-if="result" class="results-container">
        <hr />
        <div class="result-main">
          <label>Current Value</label>
          <div class="value-display">${{ result.current_value.toLocaleString(undefined, {minimumFractionDigits: 2}) }}</div>
        </div>

        <div class="result-grid">
          <div class="result-item">
            <span class="label">Total Return</span>
            <span class="value">${{ result.total_return.toFixed(2) }}</span>
          </div>
          <div class="result-item">
            <span class="label">Performance</span>
            <span :class="['percent', result.return_percentage >= 0 ? 'positive' : 'negative']">
              {{ result.return_percentage >= 0 ? '▲' : '▼' }} {{ result.return_percentage.toFixed(2) }}%
            </span>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from "vue";
import axios from "axios";

const startDate = ref("");
const startAmount = ref(0);
const result = ref(null);
const error = ref("");

const calculateLumpSum = async () => {
  error.value = "";
  try {
    const response = await axios.post("http://127.0.0.1:8000/calculate_lump_sum", {
      start_date: startDate.value,
      start_amount: parseFloat(startAmount.value)
    });
    result.value = response.data;
  } catch (err) {
    error.value = err.response?.data?.detail || "An error occurred";
    result.value = null;
  }
};
</script>

<style scoped>
.widget-card {
  background: #ffffff;
  border-radius: 12px;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
  padding: 1.5rem;
  max-width: 400px;
  font-family: sans-serif;
  border: 1px solid #eef2f6;
}

.widget-header h3 {
  margin: 0;
  color: #1a202c;
  font-size: 1.25rem;
}

.subtitle {
  font-size: 0.8rem;
  color: #718096;
}

.widget-body {
  margin-top: 1.5rem;
}

.input-grid {
  display: flex;
  flex-direction: column;
  gap: 1rem;
  margin-bottom: 1.5rem;
}

.input-group label {
  display: block;
  font-size: 0.85rem;
  font-weight: 600;
  color: #4a5568;
  margin-bottom: 0.4rem;
}

.input-group input {
  width: 100%;
  padding: 0.6rem;
  border: 1px solid #cbd5e0;
  border-radius: 6px;
  box-sizing: border-box; /* Ensures padding doesn't break width */
}

.calc-button {
  width: 100%;
  padding: 0.8rem;
  background-color: #3182ce;
  color: white;
  border: none;
  border-radius: 6px;
  font-weight: bold;
  cursor: pointer;
  transition: background 0.2s;
}

.calc-button:hover {
  background-color: #2b6cb0;
}

.results-container {
  margin-top: 1.5rem;
}

.result-main {
  text-align: center;
  margin: 1rem 0;
}

.value-display {
  font-size: 1.8rem;
  font-weight: bold;
  color: #2d3748;
}

.result-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 10px;
  margin-top: 1rem;
}

.result-item {
  background: #f7fafc;
  padding: 0.8rem;
  border-radius: 8px;
  text-align: center;
}

.label {
  display: block;
  font-size: 0.75rem;
  color: #718096;
  text-transform: uppercase;
}

.percent {
  font-weight: bold;
}

.positive { color: #38a169; }
.negative { color: #e53e3e; }

.error-banner {
  background: #fff5f5;
  color: #c53030;
  padding: 0.5rem;
  border-radius: 4px;
  margin-top: 1rem;
  font-size: 0.9rem;
}
</style>