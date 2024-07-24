// script.js

document.addEventListener('DOMContentLoaded', function() {
    const parkingLots = [
      { id: 1, name: 'Parking Lot A', available: true },
      { id: 2, name: 'Parking Lot B', available: true },
      { id: 3, name: 'Parking Lot C', available: true }
    ];
  
    const parkingLotList = document.getElementById('parkingLotList');
    const reservationForm = document.getElementById('reservationForm');
  
    // Mostrar los estacionamientos disponibles
    parkingLots.forEach(lot => {
      const li = document.createElement('li');
      li.textContent = lot.name;
      li.classList.add('parking-lot');
      if (!lot.available) {
        li.classList.add('not-available');
      }
      parkingLotList.appendChild(li);
    });
  
    // Manejar la reserva cuando se envíe el formulario
    reservationForm.addEventListener('submit', function(event) {
      event.preventDefault();
      
      const name = document.getElementById('name').value;
      const email = document.getElementById('email').value;
      const parkingLot = document.getElementById('parkingLot').value;
  
      if (!name || !email || !parkingLot) {
        alert('Please fill out all fields.');
        return;
      }
  
      alert(`Reservation made for ${name} (${email}) in ${parkingLot}`);
    
  
      // Reiniciar el formulario después de la reserva
      reservationForm.reset();
    });
  });
  

  $(document).ready(function() {
    // Obtener los estacionamientos disponibles desde el servidor
    $.get('/api/parking-lots/', function(data) {
      // Llenar la lista desplegable con los estacionamientos disponibles
      var parkingLotSelect = $('#parkingLot');
      data.forEach(function(parkingLot) {
        parkingLotSelect.append('<option value="' + parkingLot.id + '">' + parkingLot.nombre + '</option>');
      });
    });
  
    // Agregar un manejador de eventos para el formulario de reserva
    $('#reservationForm').on('submit', function(event) {
      event.preventDefault();
  
      // Obtener los valores del formulario
      var formData = {
        name: $('#name').val(),
        email: $('#email').val(),
        parking_lot: $('#parkingLot').val()
      };
  
      // Enviar la reserva al servidor
      $.post('/api/reservations/', formData, function(response) {
        // Manipular la respuesta del servidor
        console.log(response);
        // Limpiar el formulario
        $('#reservationForm')[0].reset();
      });
    });
  });