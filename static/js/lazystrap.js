function validateForm(query)
  {
    return (query.length > 2);
  }

function set_years(startYear) {
  var y = new Date().getFullYear();
  document.getElementById('years').innerHTML = startYear + "-" + y;
}

$(document.links).filter(function() {
  return this.hostname != window.location.hostname;
}).attr('target', '_blank');