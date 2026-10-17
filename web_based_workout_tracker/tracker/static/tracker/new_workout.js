document.addEventListener('DOMContentLoaded', function(){
    let container = document.querySelector('#exercise_container');
    let add_button = document.querySelector('#add_exercise');

    add_button.addEventListener("click", function(){
        let firstExercise = document.querySelector('.exercise');
        let newExercise = firstExercise.cloneNode(true);
        newExercise.querySelectorAll("input").forEach(input => {input.value = "";})
        container.append(newExercise);
    })

});