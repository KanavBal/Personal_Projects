
// Hiding the list of exercises by defult and showing them when button is clicked
document.addEventListener('DOMContentLoaded', function(){
    document.querySelector('#current').style.display = 'none';
    let viewButton = document.querySelector('#view');
    viewButton.onclick = function(){
        document.querySelector('#current').style.display = 'block';
    }
    
});