console.log("search_page_function.js loaded.")
var searchTextbox = document.getElementById('search_box_id');
var prevButton = document.getElementById('prev_result_button_id');
var nextButton = document.getElementById('next_result_button_id');

var elementsWithTargetString = [];
var elementListLength = 0;
var index = 0;

//var elementsToSearch = document.body.getElementsByTagName('p');
var elementsToSearch = document.body.querySelectorAll("h1,h2,h3,h4,h5,h6,p,li,pre");
//var elementsToSearch = document.body.querySelectorAll("p,li,pre");

// Search Button
searchTextbox.addEventListener('keypress', function(event){
    console.log('Search initated.');
    index = 0;
    elementListLength = 0;
    elementsWithTargetString = [];

    prev_and_next_button_visibility(false);
    remove_highlights();

    var targetString = searchTextbox.value.toLowerCase().trim();
    //    console.log("Total number of search elements: " + elementsToSearch.length + ". Searching for: " + targetString);
    console.log("Searching for: " + targetString);

    if(targetString.length == 0){
        console.log("Target string is empty.")
        remove_highlights();
        return;
    };

    for(let i = 0; i < elementsToSearch.length; i++){
        var currentElement = elementsToSearch[i];
        if(currentElement.innerText.toLowerCase().search(targetString) >= 0){
            console.log("Located a match.");
            elementsWithTargetString.push(currentElement);
        };
    };

    elementListLength = elementsWithTargetString.length;

    if(elementListLength > 0){
        highlight_search_results();
        elementsWithTargetString[index].scrollIntoView({block:"center"});
        elementsWithTargetString[index].style.backgroundColor="lime";
        prev_and_next_button_visibility(true);
    };
});

// Previous Search Result Button
prevButton.addEventListener('click', function(event){
    elementsWithTargetString[index].style.backgroundColor="yellow";
    index = index-1;
    if(index < 0){
        index = elementListLength - 1;
    };
    elementsWithTargetString[index].scrollIntoView({block:"center"});
    elementsWithTargetString[index].style.backgroundColor="lime";
});

// Next Search Result Button
nextButton.addEventListener('click', function(event){
    elementsWithTargetString[index].style.backgroundColor="yellow";
    index = index+1;
    if(index >= elementListLength){
        index = 0;
    };
    elementsWithTargetString[index].scrollIntoView({block:"center"});
    elementsWithTargetString[index].style.backgroundColor="lime";
});

// Hide/Show Prev and Next Buttons
function prev_and_next_button_visibility(show_buttons=true){
    if(show_buttons){
        prevButton.removeAttribute('hidden');
        nextButton.removeAttribute('hidden');
    }else{
        prevButton.setAttribute('hidden','hidden');
        nextButton.setAttribute('hidden','hidden');
    };
};

// Highlight Search Results
function highlight_search_results(){
    for(let i = 0; i < elementListLength; i++){
        elementsWithTargetString[i].style.backgroundColor="yellow";
    };
};

// Remove Highlight
function remove_highlights(){
    for(let i = 0; i < elementsToSearch.length; i++){
        elementsToSearch[i].style.backgroundColor="";
    };
};