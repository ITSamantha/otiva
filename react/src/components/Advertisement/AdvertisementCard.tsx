import React, { useEffect, useState } from 'react';
import { Link, useNavigate, useParams } from 'react-router-dom';
import {
  addToFavorites,
  deleteAdvertisement,
  deleteFromFavorites,
  getAdvertisementById,
  getChatId
} from '../../service/dataService';
import Loader from '../Loader';
import { Button } from '@mui/material';
import FavoriteBorderIcon from '@mui/icons-material/FavoriteBorder';
import FavoriteIcon from '@mui/icons-material/Favorite';
import { useDispatch, useSelector } from 'react-redux';
import { fetchMyUser, selectMyUser } from '../../redux/slices/MyUserSlice';
import ReviewBlock from '../Review/ReviewBlock';
import DeleteOutlineIcon from '@mui/icons-material/DeleteOutline';
import PhotoSlider from '../PhotoSlider/PhotoSlider';

const AdvertisementCard = () => {
  const { id } = useParams();
  const [ad, setAd] = useState<AdInfo | null>(null);
  const user = useSelector(selectMyUser);
  const dispatch = useDispatch();
  const [isFavourite, setIsFavourite] = useState<boolean>();
  const navigate = useNavigate();

  const photos = [
    'https://http.cat/300',
    'https://http.cat/200',
    'https://http.cat/300',
    'https://http.cat/300'
  ];

  useEffect(() => {
    async function fetchData() {
      let data = await getAdvertisementById(Number(id));
      await dispatch(fetchMyUser() as any);
      setAd(data);
      if (user) {
        const isFav = user.ad_favourites.some((ad: AdInfo) => ad.id === Number(id));
        setIsFavourite(isFav);
      }
    }

    fetchData();
  }, [dispatch, id]);

  const handleFavorite = async () => {
    setIsFavourite(true);
    await addToFavorites(Number(id));
    await dispatch(fetchMyUser() as any);
  };

  const handleUnfavorite = async () => {
    setIsFavourite(false);
    await deleteFromFavorites(Number(id));
    await dispatch(fetchMyUser() as any);
  };

  const handleGetChatId = async () => {
    const chatId = await getChatId(ad!.user.id);
    navigate(`/chat/${chatId.id}`);
  };

  const handleDelete = async () => {
    deleteAdvertisement(ad!.id);
  };

  if (!ad) {
    return <Loader />;
  }

  return (
    <div className="AdvertisementCard">
      <div className="container">
        <div className="AdvertisementCard__Wrapper">
          <div className="AdvertisementCard__Photos">
            <PhotoSlider photos={photos} />

          </div>
          <div className="AdvertisementCard__Content">
            <div className="AdvertisementCard__Main">
              <h1>{ad.title}</h1>
              <div className="AdvertisementCard__Price">
                ₪ {ad.price}
              </div>
            </div>
            <div className="AdvertisementCard__Tag">{ad.ad_type.title}</div>
            <div className="AdvertisementCard__Tag">{ad.category.title}</div>


            <p>{ad.user_description}</p>
            <div>{ad.created_at_str}</div>
            <Link to={`/profile/${ad.user.id}`}>
              <div>
                Seller: {ad.user.first_name} {ad.user.last_name}
              </div>
            </Link>
            {isFavourite ? (
              <Button onClick={handleUnfavorite}>
                <FavoriteIcon />
              </Button>
            ) : (
              <Button onClick={handleFavorite}>
                <FavoriteBorderIcon />
              </Button>
            )}
            {user && user.id !== ad.user.id ? (
              <Button onClick={handleGetChatId}>Contact the seller</Button>
            ) : (
              <Button onClick={handleDelete}>
                <DeleteOutlineIcon />
              </Button>
            )}

            <ReviewBlock reviews={ad.reviews} />
          </div>
        </div>
      </div>
    </div>
  );
};

export default AdvertisementCard;
