import { useEffect, useState } from 'react';
import axios from 'axios';

function App() {
  const [data, setData] = useState(null);

  useEffect(() => {
    axios.get('/api').then((response) => {
      setData(response.data);
    });
  }, []);

  return (
    <div>
      <h1>Simple Express App</h1>
      <h2>{data}</h2>
    </div>
  );
}