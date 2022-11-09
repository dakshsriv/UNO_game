import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import Dashboard from './components/Dashboard';
import { CookiesProvider } from "react-cookie";
import Login from './components/Login'

import {
  createBrowserRouter,
  RouterProvider,
} from "react-router-dom";

import reportWebVitals from './reportWebVitals';

const router = createBrowserRouter([
  {
    path: "/",
    element: <Dashboard userID=""/>,
  },
  {
    path: "/login/",
    element: <Login/>,
  },
]);

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <CookiesProvider>
    <RouterProvider router={router}/>
    </CookiesProvider>
  </React.StrictMode>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
