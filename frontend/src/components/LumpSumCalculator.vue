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
          <div class="value-display">${{ result.current_value.toLocaleString(undefined, { minimumFractionDigits: 2 }) }}
          </div>
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
    // Ensure this URL matches your FastAPI backend
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
  padding: clamp(1.5rem, 2.5vw, 2rem);
  width: 100%;
  font-family: sans-serif;
  border: 1px solid #eef2f6;
  box-sizing: border-box;
}

.widget-header h3 {
  margin: 0;
  color: #1a202c;
  font-size: clamp(1.15rem, 2vw, 1.5rem);
  font-weight: 700;
}

.subtitle {
  font-size: clamp(0.75rem, 1.2vw, 0.875rem);
  color: #718096;
  font-weight: 500;
}

.widget-body {
  margin-top: 1.5rem;
}

.input-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 1.5rem;
  margin-bottom: 1.5rem;
}

.input-group label {
  display: block;
  font-size: 0.875rem;
  font-weight: 600;
  color: #4a5568;
  margin-bottom: 0.5rem;
}

.input-group input {
  width: 100%;
  padding: 0.75rem;
  border: 1.5px solid #cbd5e0;
  border-radius: 8px;
  box-sizing: border-box;
  font-size: 1rem;
  transition: all 0.2s ease;
}

/* Ensure 'focus' is spelled correctly and brackets are closed */
.input-group input:focus {
  outline: none;
  border-color: #3182ce;
  box-shadow: 0 0 0 3px rgba(49, 130, 206, 0.1);
}

.calc-button {
  width: 100%;
  max-width: 300px;
  padding: 0.875rem 1.5rem;
  background-color: #3182ce;
  color: white;
  border: none;
  border-radius: 8px;
  font-weight: 600;
  font-size: 1rem;
  cursor: pointer;
  transition: all 0.3s ease;
  box-shadow: 0 2px 4px rgba(49, 130, 206, 0.2);
}

.calc-button:hover {
  background-color: #2b6cb0;
  transform: translateY(-1px);
  box-shadow: 0 4px 8px rgba(49, 130, 206, 0.3);
}

.calc-button:active {
  transform: translateY(0);
}

.results-container {
  margin-top: 2rem;
}

.results-container hr {
  border: none;
  border-top: 1px solid #e2e8f0;
  margin: 1.5rem 0;
}

.result-main {
  text-align: center;
  margin: 1.5rem 0;
}

.result-main label {
  display: block;
  font-size: 0.875rem;
  color: #718096;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  font-weight: 600;
  margin-bottom: 0.5rem;
}

.value-display {
  font-size: clamp(2rem, 3.5vw, 2.5rem);
  font-weight: 700;
  color: #2d3748;
  letter-spacing: -0.02em;
}

.result-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 1rem;
  margin-top: 1.5rem;
}

.result-item {
  background: #f7fafc;
  padding: 1.25rem;
  border-radius: 10px;
  text-align: center;
  border: 1px solid #e2e8f0;
  transition: all 0.2s ease;
}

.result-item:hover {
  background: #edf2f7;
  transform: translateY(-2px);
}

.label {
  display: block;
  font-size: 0.75rem;
  color: #718096;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  font-weight: 600;
  margin-bottom: 0.5rem;
}

.result-item .value {
  display: block;
  font-size: 1.5rem;
  font-weight: 700;
  color: #2d3748;
  margin-top: 0.25rem;
}

.percent {
  display: block;
  font-size: 1.5rem;
  font-weight: 700;
  margin-top: 0.25rem;
}

.positive {
  color: #38a169;
}

.negative {
  color: #e53e3e;
}

.error-banner {
  background: #fff5f5;
  color: #c53030;
  padding: 0.875rem 1rem;
  border-radius: 8px;
  margin-top: 1rem;
  font-size: 0.9375rem;
  border: 1px solid #feb2b2;
}

/* Responsive */
@media (max-width: 768px) {
  .input-grid {
    grid-template-columns: 1fr;
  }
  
  .result-grid {
    grid-template-columns: 1fr;
  }
  
  .calc-button {
    max-width: 100%;
  }
}
</style>