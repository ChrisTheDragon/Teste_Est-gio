<template>
    <div class="search-container">
      <h1>Busca de Operadoras de Saúde</h1>
      <input 
        v-model="searchTerm" 
        @input="performSearch" 
        placeholder="Digite o nome ou código da operadora..."
      />
      
      <div v-if="loading" class="loading">Carregando...</div>
      
      <div v-if="results.length > 0" class="results">
        <div v-for="item in results" :key="item.REG_ANS" class="result-item">
          <h3>{{ item.DESCRICAO }}</h3>
          <p><strong>Código:</strong> {{ item.CD_CONTA_CONTABIL }}</p>
          <p><strong>Registro ANS:</strong> {{ item.REG_ANS }}</p>
          <p><strong>Saldo Inicial:</strong> R$ {{ item.VL_SALDO_INICIAL }}</p>
          <p><strong>Saldo Final:</strong> R$ {{ item.VL_SALDO_FINAL }}</p>
        </div>
      </div>
      
      <div v-else-if="searchTerm && !loading" class="no-results">
        Nenhum resultado encontrado para "{{ searchTerm }}"
      </div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        searchTerm: '',
        results: [],
        loading: false,
        debounce: null
      }
    },
    methods: {
      performSearch() {
        clearTimeout(this.debounce)
        
        if (this.searchTerm.length < 2) {
          this.results = []
          return
        }
        
        this.loading = true
        
        this.debounce = setTimeout(async () => {
          try {
            const response = await fetch(`http://localhost:5000/api/search?q=${encodeURIComponent(this.searchTerm)}`)
            this.results = await response.json()
          } catch (error) {
            console.error('Erro na busca:', error)
          } finally {
            this.loading = false
          }
        }, 300)
      }
    }
  }
  </script>
  
  <style scoped>
  .search-container {
    max-width: 800px;
    margin: 0 auto;
    padding: 20px;
  }
  
  input {
    width: 100%;
    padding: 10px;
    font-size: 16px;
    margin-bottom: 20px;
  }
  
  .result-item {
    background: #f5f5f5;
    padding: 15px;
    margin-bottom: 10px;
    border-radius: 5px;
  }
  
  .loading {
    text-align: center;
    padding: 20px;
  }
  
  .no-results {
    text-align: center;
    padding: 20px;
    color: #666;
  }
  </style>