



const myDiv = document.querySelector('#navMobile');




function adjustClass() {
  if (window.innerWidth <= 768) { 
      myDiv.classList.remove('hideDiv');
      myDiv.classList.add('d-flex');
      myDiv.classList.add('justify-content-end');
      console.log("wowowowowo")
  } else {
      myDiv.classList.remove('d-flex');
      myDiv.classList.remove('justify-content-end');
      myDiv.classList.add('hideDiv');
      console.log("else")
  }
}


adjustClass();


window.addEventListener('resize', adjustClass);
