import React from 'react';
import ReactDOM from 'react-dom/client';
import GridOverlay from './components/grid-overlay';
import ApiKeyChecker from './components/api-key-checker';
import './scss/_index.scss';

ReactDOM.createRoot(document.getElementById('root')!).render(
  <React.StrictMode>
    <GridOverlay />
    <ApiKeyChecker/>
  </React.StrictMode>,
)
