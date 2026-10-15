document.addEventListener('DOMContentLoaded', function(){
    // Starting by hiding the list if all exercises
    document.querySelector('#current').style.display = 'none';
    
    let viewButton = document.querySelector('#view');
    viewButton.onclick = function(){
        document.querySelector('#current').style.display = 'block';
    }
    
});