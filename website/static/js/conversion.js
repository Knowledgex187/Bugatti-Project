document.addEventListener('DOMContentLoaded', function () {
    document.getElementById('miles').addEventListener('click', function () {
      const mph = parseFloat(document.getElementById('mph').value);
      if (!isNaN(mph)) {
        const ms = mph * 0.44704; // Conversion factor from mph to m/s
        document.getElementById('ms').value = ms.toFixed(2);
      }
    });
  
    document.getElementById('kilometers').addEventListener('click', function () {
      const kmh = parseFloat(document.getElementById('kmh').value);
      if (!isNaN(kmh)) {
        const ms1 = kmh / 3.6; // Conversion factor from km/h to m/s
        document.getElementById('ms1').value = ms1.toFixed(2);
      }
    });
  });
  