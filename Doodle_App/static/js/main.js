window.addEventListener('load', () => {
    const canvas = document.querySelector("#drawingCanvas");
    const context = canvas.getContext("2d");

    //Resizing
    canvas.height = 250;
    canvas.width = 600;

    //variables
    let painting = false;

    function startPosition(){
        painting = true;
    }
    function endPosition(){
        painting = false;
    }
    //EventListeners

});