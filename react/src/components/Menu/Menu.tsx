import { useDispatch, useSelector } from 'react-redux';
import { Link, useNavigate } from 'react-router-dom';
import { logoutUser, selectMyUser } from '../../redux/slices/MyUserSlice';
import { Button } from '@mui/material';
import { useEffect } from 'react';

const Menu = () => {
  const user = useSelector(selectMyUser);

  const dispatch = useDispatch();
  const navigate = useNavigate();

  return (
    <header className="Header">
      <div className="container">
        <div className="Header__Wrapper">
          <div className="Header__Logo">
            <Link to="/">
              <img src="/images/Logo.png" alt="Logo" />
            </Link>
          </div>
          <div className="Header__Navbar">
            <>
              <Link to="/" className="Header__Navbar__Item">
                Advertisements
              </Link>
              <Link to="/upload-form" className="Header__Navbar__Item">
                Upload
              </Link>
              {user && (
                <>
                  <Link to="/chats" className="Header__Navbar__Item">
                    Chats
                  </Link>
                </>
              )}
            </>
          </div>
          <div className="Header__Auth">
            {user ? (
              <Link to={`/profile/${user.id}`} className="Header__Auth__Button">
                Profile
              </Link>
            ) : (
              <Link to="/login" className="Header__Auth__Button">
                Login
              </Link>
            )}
          </div>
        </div>
      </div>
    </header>
    // <header className="global-navigation-site-header">
    //   <div className="global-navigation-site-header-container">
    //     <section className="global-navigation-row primary">
    //       <div className=" global-navigation-row-container">
    //         <div className="header-row uitk-layout-flex uitk-layout-flex-align-items-center uitk-layout-flex-flex-wrap-nowrap uitk-spacing uitk-spacing-margin-unset uitk-spacing-padding-inlinestart-six uitk-spacing-padding-small-inlineend-three uitk-spacing-padding-medium-inlineend-three uitk-spacing-padding-large-inlineend-two uitk-spacing-padding-extra_large-inlineend-two uitk-layout-flex-item uitk-layout-flex-item-flex-grow-1">
    //           <div>
    //             <Link to="/" className="uitk-header-brand-logo">
    //               <img
    //                 src="https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_92x30dp.png"
    //                 alt="logo"
    //               />
    //             </Link>
    //             <div
    //               className="uitk-layout-flex uitk-layout-flex-align-items-center uitk-layout-flex-justify-content-flex-start uitk-layout-flex-flex-wrap-nowrap uitk-spacing uitk-spacing-padding-inlinestart-one uitk-layout-flex-item uitk-layout-flex-item-flex-basis-half_width uitk-layout-flex-item-flex-grow-1"
    //               id="primary-navigation"
    //             />
    //           </div>
    //           {user && (
    //             <div>
    //               {user.id && (
    //                 <Link to={`/profile/${user.id}`}>
    //                   <Button variant="contained">Profile</Button>
    //                 </Link>
    //               )}
    //               <Link to="/upload-form">
    //                 <Button variant="contained">Upload</Button>
    //               </Link>
    //               <Link to="/chats">
    //                 <Button variant="contained">My chats</Button>
    //               </Link>
    //               <Button variant="contained" onClick={handleLogout}>
    //                 Logout
    //               </Button>
    //             </div>
    //           )}
    //
    //           {!user && (
    //             <Link to="/login">
    //               <Button variant="contained">Login</Button>
    //             </Link>
    //           )}
    //         </div>
    //       </div>
    //     </section>
    //   </div>
    // </header>
  );
};

export default Menu;
