
// eslint-disable-next-line no-unused-vars
import React from "react";
import { useState } from "react";

// eslint-disable-next-line react/prop-types
const ParkingForm = ({ onReserve }) => {
  const [name, setName] = useState('');
  const [time, setTime] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    onReserve({ name, time });
    setName('');
    setTime('');
  };

  return (
    <form onSubmit={handleSubmit}>
      <input
        type="text"
        placeholder="Your Name"
        value={name}
        onChange={(e) => setName(e.target.value)}
      />
      <input
        type="text"
        placeholder="Reservation Time"
        value={time}
        onChange={(e) => setTime(e.target.value)}
      />
      <button type="submit">Reserve Parking</button>
    </form>
  );
};

export default ParkingForm;
