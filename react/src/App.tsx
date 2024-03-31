import React from 'react';
import { createBrowserRouter, RouterProvider } from 'react-router-dom';
import RouterWrapper from './RouterWrapper';
import Login from './components/Login/Login';
import './scss/main.scss';
import Home from './pages/Home';
import Upload from './pages/Upload';
import { GoogleOAuthProvider } from '@react-oauth/google';
import Register from './components/Register/Register';
import Catalog from './components/Catalog/CategoriesBlock';
import MapWrapper from './pages/Map';
import Profile from './pages/profile/Profile';
import ProfileEdit from './pages/profile/ProfileEdit';
import ProfilePhone from './pages/profile/ProfilePhone';
import AdvertisementCard from './components/Advertisement/AdvertisementCard';
import Category from './pages/Category';
import ProfileAllAdvertisements from './pages/profile/ProfileAllAdvertisements';

export const APP_URL = 'http://localhost:3000/';

function App() {
  const router = createBrowserRouter([
    {
      path: '/',
      element: (
        <RouterWrapper>
          <Home />
        </RouterWrapper>
      )
    },
    {
      path: '/category/:id',
      element: (
        <RouterWrapper>
          <Category />
        </RouterWrapper>
      )
    },
    {
      path: '/login',
      element: (
        <RouterWrapper>
          <Login />
        </RouterWrapper>
      )
    },
    {
      path: 'category/:categorySlug',
      element: (
        <RouterWrapper>
          <Catalog />
        </RouterWrapper>
      )
    },
    {
      path: 'advertisement/:id',
      element: (
        <RouterWrapper>
          <AdvertisementCard />
        </RouterWrapper>
      )
    },
    {
      path: 'upload-form',
      element: (
        <RouterWrapper>
          <Upload />
        </RouterWrapper>
      )
    },
    {
      path: '/profile/:id',
      element: (
        <RouterWrapper>
          <Profile />
        </RouterWrapper>
      )
    },
    {
      path: '/profile/:id/advertisements',
      element: (
        <RouterWrapper>
          <ProfileAllAdvertisements />
        </RouterWrapper>
      )
    },
    {
      path: '/register',
      element: (
        <RouterWrapper>
          <Register />
        </RouterWrapper>
      )
    },
    {
      path: '/map',
      element: (
        <RouterWrapper>
          <MapWrapper />
        </RouterWrapper>
      )
    },
    {
      path: '/profile/edit',
      element: (
        <RouterWrapper>
          <ProfileEdit />
        </RouterWrapper>
      )
    },
    {
      path: '/profile/phone',
      element: (
        <RouterWrapper>
          <ProfilePhone />
        </RouterWrapper>
      )
    }
  ]);

  return (
    <>
      <GoogleOAuthProvider clientId={process.env.REACT_APP_CLIENT_ID || '123'}>
        <React.StrictMode>
          <RouterProvider router={router} />
        </React.StrictMode>
      </GoogleOAuthProvider>
    </>
  );
}

export default App;
