import React, { useState, useEffect } from 'react';
import axios from 'axios';

function App() {
  const [products, setProducts] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');

  useEffect(() => {
    axios.get('http://localhost:5000/products')
      .then(response => {
        setProducts(response.data);
        setLoading(false);
      })
      .catch(error => {
        setError('Failed to fetch products');
        console.error('Error fetching products:', error);
        setLoading(false);
      });
  }, []);

  return (
    <div style={styles.container}>
      <h1 style={styles.header}>📦 Product Catalog</h1>

      {loading && <p>Loading products...</p>}
      {error && <p style={styles.error}>{error}</p>}

      <div style={styles.cardContainer}>
        {products.map(product => (
          <div key={product.id} style={styles.card}>
            <h3>{product.name}</h3>
            <p><strong>Price:</strong> ${product.price.toFixed(2)}</p>
            <p><small>Added: {new Date(product.created_at).toLocaleString()}</small></p>
          </div>
        ))}
      </div>
    </div>
  );
}

const styles = {
  container: {
    fontFamily: 'Arial, sans-serif',
    padding: '2rem',
    background: '#f4f4f4',
  },
  header: {
    textAlign: 'center',
    color: '#333',
  },
  error: {
    color: 'red',
    textAlign: 'center',
  },
  cardContainer: {
    display: 'flex',
    flexWrap: 'wrap',
    justifyContent: 'center',
    gap: '1rem',
    marginTop: '2rem',
  },
  card: {
    backgroundColor: '#fff',
    padding: '1rem',
    borderRadius: '10px',
    boxShadow: '0 0 8px rgba(0, 0, 0, 0.1)',
    width: '250px',
    textAlign: 'center',
  },
};

export default App;
