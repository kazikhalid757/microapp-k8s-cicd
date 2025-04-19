import React, { useState, useEffect } from 'react';
import axios from 'axios';

function App() {
  const [products, setProducts] = useState([]);

  useEffect(() => {
    axios.get('http://localhost:5000/products')
      .then(response => {
        setProducts(response.data);
      })
      .catch(error => {
        console.error('Error fetching products:', error);
      });
  }, []);

  return (
    <div className="App">
      <h1>Products</h1>
      <ul>
        {products.map((product, index) => (
          <li key={index}>
            {product[1]} - ${product[2]}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;
