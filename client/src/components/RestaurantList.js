import React, { useEffect, useState } from 'react';

function RestaurantList() {
    const [restaurants, setRestaurants] = useState([]);

    useEffect(() => {
        fetch('http://localhost:5555/restaurants')
            .then(response => response.json())
            .then(data => setRestaurants(data))
            .catch(error => console.error('Error fetching data:', error));
    }, []);

    return (
        <div>
            <h1>Restaurants</h1>
            <ul>
                {restaurants.map(restaurant => (
                    <li key={restaurant.id}>
                        {restaurant.name} - {restaurant.address}
                    </li>
                ))}
            </ul>
        </div>
    );
}

export default RestaurantList;
