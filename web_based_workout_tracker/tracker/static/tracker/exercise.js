
// Hiding the list of exercises by defult and showing them when button is clicked
document.addEventListener('DOMContentLoaded', function(){
    document.querySelector('#exercises').style.display = 'none';
    let view = false;
    let viewButton = document.querySelector('#view');
    viewButton.onclick = function(){
        if (view == false) {
            document.querySelector('#exercises').style.display = 'block';
            viewButton.innerHTML = 'Hide Current Exercises';
            view = true;
        }
        else{
            document.querySelector('#exercises').style.display = 'none';
            viewButton.innerHTML = 'View Current Exercises';
            view = false;
        }
    }
    
});