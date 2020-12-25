// For the image, .render-image-for-code
let hrefList = window.location.href.split('/')
let lengthOfHref = hrefList.length
let datasetChosen = hrefList[lengthOfHref - 1];
let algorithmChosen = hrefList[lengthOfHref - 2];
let imageHandler = document.querySelector('.render-image-for-code').src;
let findIndexFor = 'coin_change_making.png';
let indexForSubStr = imageHandler.indexOf(findIndexFor);
let extractURI = imageHandler.substr(0, indexForSubStr - 1);
let newResource = '';

if (algorithmChosen === '8') {
    newResource = 'coin_change_making.png';
} else if (algorithmChosen === '5') {
    newResource = 'knapsack_0_1.png';
} else if (algorithmChosen === '2') {
    newResource = 'levensthein_distance.png';
} else if (algorithmChosen === '3') {
    newResource = 'lis.png';
} else if (algorithmChosen === '0') {
    newResource = 'longest_common_subsequence.png';
} else if (algorithmChosen === '4') {
    newResource = 'matrix_chain_multiplication.png';
} else if (algorithmChosen === '6') {
    newResource = 'partition.png';
} else if (algorithmChosen === '7') {
    newResource = 'rod_cutting.png';
} else if (algorithmChosen === '1') {
    newResource = 'shortest_common_supersequence.png';
} else if (algorithmChosen === '9') {
    newResource = 'word_break.png';
}

extractURI = `${extractURI}/${newResource}`;

document.querySelector('.render-image-for-code').src = extractURI;

// For the test cases, .test-case-box
let testSampleHandler = document.querySelector('.test-case-box');
let stringFormatter = '';
let datasetChosenSelected = '';

if (datasetChosen === '8') {
    datasetChosenSelected = coin_change_making_template_test_case;
} else if (datasetChosen === '5') {
    datasetChosenSelected = knapsack_0_1_template;
} else if (datasetChosen === '2') {
    datasetChosenSelected = levensthein_distance_template;
} else if (datasetChosen === '3') {
    datasetChosenSelected = longest_increasing_subsequence_template;
} else if (datasetChosen === '0') {
    datasetChosenSelected = longest_common_subsequence_template;
} else if (datasetChosen === '4') {
    datasetChosenSelected = matrix_chain_multiplication_template;
} else if (datasetChosen === '6') {
    datasetChosenSelected = partition_template;
} else if (datasetChosen === '7') {
    datasetChosenSelected = rod_cutting_template;
} else if (datasetChosen === '1') {
    datasetChosenSelected = shortest_common_supersequence_template;
} else if (datasetChosen === '9') {
    datasetChosenSelected = word_break_template;
}

for (let i = 0; i < datasetChosenSelected.length; ++i) {
    stringFormatter = "<p>" + stringFormatter + datasetChosenSelected[i] + "</p>";
}

testSampleHandler.innerHTML = stringFormatter;
