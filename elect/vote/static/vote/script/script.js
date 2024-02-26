
input = document.querySelector('#input-location');
button = document.querySelector('#location-btn');
parties = document.querySelectorAll(".votes");

input.addEventListener("input", (e) => {
  let local = e.target.value;
  if (local.length <= 0) {
    button.disabled = true;
  }
  else {
    button.disabled = false;
  }
})

for (let party of parties) {
  let votes = Number(party.dataset.votes);
  anime({
    targets: party,
    textContent: [0, votes],
    round: 1,
    easing: 'easeInOutExpo'
  });
}

