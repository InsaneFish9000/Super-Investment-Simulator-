<template>
    <div class="dashboard-wrapper">
        <header class="dashboard-header">
            <div class="header-content">
                <h1>Investment Overview</h1>
                <p class="date-display">{{ currentDate }}</p>
            </div>
            <button class="refresh-btn" @click="refreshData">
                <span class="refresh-icon">↻</span>
                Refresh Data
            </button>
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
                <span class="stat-subtext">Initial capital</span>
            </div>
            <div class="stat-card">
                <span class="stat-label">Overall Profit</span>
                <div class="stat-value profit">+$4,500.00</div>
                <span class="stat-change positive">+22.5% ROI</span>
            </div>
        </section>

        <section class="calculator-section">
            <LumpSumCalculator />
        </section>
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
    margin: 0;
    padding: 1.5rem 2rem;
    width: 100%;
    /* REMOVED: max-width and auto margins to allow full stretch */
    box-sizing: border-box;
}

/* Header Section */
.dashboard-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 2rem;
    gap: 1.5rem;
    flex-wrap: wrap;
}

.header-content h1 {
    font-size: 2.5rem;
    font-weight: 700;
    margin: 0;
    color: #1a202c;
    letter-spacing: -0.02em;
}

.date-display {
    color: #718096;
    margin-top: 0.5rem;
    font-size: 1rem;
    font-weight: 500;
}

.refresh-btn {
    display: flex;
    align-items: center;
    gap: 0.5rem;
    padding: 0.75rem 1.5rem;
    background: white;
    border: 1.5px solid #e2e8f0;
    border-radius: 8px;
    cursor: pointer;
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    font-weight: 600;
    font-size: 0.9375rem;
    color: #2d3748;
    box-shadow: 0 1px 3px rgba(0, 0, 0, 0.05);
}

.refresh-btn:hover {
    background: #f7fafc;
    border-color: #cbd5e0;
    transform: translateY(-1px);
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
}

.refresh-btn:active {
    transform: translateY(0);
}

.refresh-icon {
    font-size: 1.25rem;
    transition: transform 0.6s ease;
}

.refresh-btn:hover .refresh-icon {
    transform: rotate(180deg);
}

/* Stats Grid */
.stats-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 1.5rem;
    margin-bottom: 2rem;
}

.stat-card {
    background: white;
    padding: 2rem;
    border-radius: 12px;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.04);
    border: 1px solid #eef2f6;
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    display: flex;
    flex-direction: column;
    gap: 0.5rem;
}

.stat-card:hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 20px rgba(0, 0, 0, 0.08);
    border-color: #e2e8f0;
}

.stat-label {
    font-size: 0.875rem;
    color: #718096;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    font-weight: 600;
}

.stat-value {
    font-size: 2.25rem;
    font-weight: 700;
    color: #1a202c;
    letter-spacing: -0.02em;
    margin: 0.25rem 0;
}

.profit {
    color: #38a169;
}

.stat-change {
    font-size: 0.9375rem;
    font-weight: 600;
}

.stat-subtext {
    font-size: 0.9375rem;
    color: #a0aec0;
    font-weight: 500;
}

.positive {
    color: #38a169;
}

/* Calculator Section */
.calculator-section {
    width: 100%;
    margin-bottom: 2rem;
}

/* Responsive Adjustments */
@media (max-width: 1200px) {
    .stats-grid {
        grid-template-columns: repeat(3, 1fr);
    }
    
    .header-content h1 {
        font-size: 2rem;
    }
}

@media (max-width: 900px) {
    .stats-grid {
        grid-template-columns: repeat(2, 1fr);
    }
}

@media (max-width: 768px) {
    .dashboard-wrapper {
        padding: 1.5rem 1rem;
    }
    
    .dashboard-header {
        flex-direction: column;
        align-items: flex-start;
    }
    
    .refresh-btn {
        width: 100%;
        justify-content: center;
    }
    
    .stats-grid {
        grid-template-columns: 1fr;
    }
    
    .header-content h1 {
        font-size: 1.75rem;
    }
}

@media (max-width: 480px) {
    .dashboard-wrapper {
        padding: 1rem;
    }
}
</style>