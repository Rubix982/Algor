let allDatasets = (document.querySelectorAll(`ol#datasets.gradient-list>li`))
let allAlgorithms = (document.querySelectorAll(`ol#algorithms.gradient-list>li`))
// console.log(allDatasets);
// console.log(allAlgorithms);
let algorithm = '';
let dataset = '';

function set_algorithm(event) {

    for (let i = 0; i < event.classList.length; ++i) {
        if (event.classList[i] === 'option-selected') {
            event.classList.remove('option-selected')
            algorithm = '';
            return;
        }
    }

    for (let i = 0; i < allAlgorithms.length; ++i) {
        allAlgorithms[i].classList.remove('option-selected')
    }

    event.classList.add('option-selected')
    algorithm = event.classList[0].split('-')[1];
}

function set_dataset(event) {

    for (let i = 0; i < event.classList.length; ++i) {
        if (event.classList[i] === 'option-selected') {
            event.classList.remove('option-selected')
            dataset = '';
            return;
        }
    }

    for (let i = 0; i < allDatasets.length; ++i) {
        allDatasets[i].classList.remove('option-selected')
    }

    event.classList.add('option-selected')
    dataset = event.classList[0].split('-')[1];
    return;
}

function submit_button() {

    if (algorithm !== '' && dataset !== '') {
        console.log(`Algorithm is ${algorithm}`)
        console.log(`Dataset is ${dataset}`)

        if (algorithm === 0 || algorithm === 1 || algorithm === 2) {
            if (dataset === 0 || dataset === 1 || dataset === 3) {

            } else {
                alert(`Invalid dataset chosen. You can choose either 
                the 1st, 2nd, or 3rd dataset to go with the algorithm you have chosen`)
            }
        } else if (algorithm === 3 || algorithm === 4 || algorithm === 8) {
            if (dataset === 3 || dataset === 4 || dataset === 8) {

            } else {
                alert(`Invalid dataset chosen. You can choose either 
                the 4th, 5th, or the 9th dataset to go with the algorithm you have chosen`)
            }
        } else if (algorithm === 5 || algorithm === 6 || algorithm === 7) {
            if (dataset === 5 || dataset === 6 || dataset === 7) {

            } else {
                alert(`Invalid dataset chosen. You can choose either 
                the 6th, 7th, or 8th dataset to go with the algorithm you have chosen`)
            }
        } else if (algorithm === 9) {
            if (dataset === 9) {

            } else {
                alert(`Invalid dataset chosen. Only the 10th dataset can 
                be chosen to go with the algorithm you have chosen`)
            }
        }
    } else {
        alert('Please choose the options from both the lists')
    }
}