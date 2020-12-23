let allDatasets = (document.querySelectorAll(`ol#datasets.gradient-list>li`))
let allAlgorithms = (document.querySelectorAll(`ol#algorithms.gradient-list>li`))
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
        if (algorithm === '0' || algorithm === '1' || algorithm === '2') {
            if (dataset === '0' || dataset === '1' || dataset === '3') {
                window.location.replace(`${window.location.href}result/${algorithm}/${dataset}`)
            } else {
                alert(`Invalid dataset chosen. You can choose either 
the 1st, 2nd, or 3rd dataset to go with the algorithm you have chosen`)
            }
        } else if (algorithm === '3' || algorithm === '4' || algorithm === '8') {
            if (dataset === '3' || dataset === '4' || dataset === '8') {
                window.location.replace(`${window.location.href}result/${algorithm}/${dataset}`)
            } else {
                alert(`Invalid dataset chosen. You can choose either 
the 4th, 5th, or the 9th dataset to go with the algorithm you have chosen`)
            }
        } else if (algorithm === '5' || algorithm === '6' || algorithm === '7') {
            if (dataset === '5' || dataset === '6' || dataset === '7') {
                window.location.replace(`${window.location.href}result/${algorithm}/${dataset}`)
            } else {
                alert(`Invalid dataset chosen. You can choose either 
the 6th, 7th, or 8th dataset to go with the algorithm you have chosen`)
            }
        } else if (algorithm === '9') {
            if (dataset === '9') {
                window.location.replace(`${window.location.href}result/${algorithm}/${dataset}`)
            } else {
                alert(`Invalid dataset chosen. Only the 10th dataset can 
be chosen to go with the algorithm you have chosen`)
            }
        }
    } else {
        alert('Please choose the options from both the lists')
    }
}

if (window.location.href.includes('/result/')) {
    let hrefList = window.location.href.split('/')
    let lengthOfHref = hrefList.length
    let dataset = hrefList[lengthOfHref - 1];
    let algorithm = hrefList[lengthOfHref - 2];
    let imageHandler = document.querySelector('.render-image-for-code').src;
    let findIndexFor = 'coin_change_making.png';
    let indexForSubStr = imageHandler.indexOf(findIndexFor);
    let extractURI = imageHandler.substr(0, indexForSubStr - 1);
    let newResource = '';

    console.log(`Algorithm is ${algorithm}`)
    console.log(`Dataset is ${dataset}`)

    if (algorithm === '0') {
        newResource = 'coin_change_making.png';
    } else if (algorithm === '1') {
        newResource = 'knapsack_01.png';
    } else if (algorithm === '2') {
        newResource = 'levensthein.png';
    } else if (algorithm === '3') {
        newResource = 'lis.png';
    } else if (algorithm === '4') {
        newResource = 'longest_common_subsequence.png';
    } else if (algorithm === '5') {
        newResource = 'matrix_chain_multiplication.png';
    } else if (algorithm === '6') {
        newResource = 'partition.png';
    } else if (algorithm === '7') {
        newResource = 'rod_cutting.png';
    } else if (algorithm === '8') {
        newResource = 'shortest_common_supersequence.png';
    } else if (algorithm === '9') {
        newResource = 'word_break.png';
    }

    extractURI = `${extractURI}/${newResource}`;

    document.querySelector('.render-image-for-code').src = extractURI;
}
