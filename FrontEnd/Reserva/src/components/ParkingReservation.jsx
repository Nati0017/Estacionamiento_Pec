import React from 'react';

import './ParkingReservation.css'; 

const ParkingReservation = () => {
  const [selectedParking, setSelectedParking] = useState(null);

  const handleParkingSelection = (parkingId) => {
    setSelectedParking(parkingId);
  };

  const handleReservationSubmit = () => {
    // Aquí podrías enviar los datos de la reserva, por ejemplo a través de una API
    console.log(`Reservando estacionamiento ${selectedParking}`);
  };

  return (
    <div className="parking-reservation">
      <h2>Reserva de Estacionamiento</h2>
      <div className="parking-list">
        <div
          className={`parking-option ${selectedParking === 1 ? 'selected' : ''}`}
          onClick={() => handleParkingSelection(1)}
        >
          Estacionamiento 1
        </div>
        <div
          className={`parking-option ${selectedParking === 2 ? 'selected' : ''}`}
          onClick={() => handleParkingSelection(2)}
        >
          Estacionamiento 2
        </div>
        <div
          className={`parking-option ${selectedParking === 3 ? 'selected' : ''}`}
          onClick={() => handleParkingSelection(3)}
        >
          Estacionamiento 3
        </div>
      </div>
      <button onClick={handleReservationSubmit} disabled={!selectedParking}>
        Reservar
      </button>
    </div>
  );
};

export default ParkingReservation;
