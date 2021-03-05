window.addEventListener('load', () => {
    
    
    const canvas = document.getElementById("canvas");
    const color_field = document.querySelectorAll(".color-field");
    // const clear = document.getElementsByClassName(".clearButton")
    // const colorRange = document.getElementsByClassName(".color-range")
    // canvas.width = 600;
    // canvas.height = 600;
    
    let context = canvas.getContext("2d");
    let start_background_color = "white";
    context.fillStyle = start_background_color;
    context.fillRect(0,0, canvas.width, canvas.height);
    
    
    let draw_color = "black";
    let draw_width = "2";
    let is_drawing = false;
    // function clear_canvas(e){
    //     console.log("clicking")
    //     context.fillStyle = start_background_color;
    //     context.clearRect(0,0, canvas.width, canvas.height);
    //     context.fillRect(0,0, canvas.width, canvas.height);
    // }
    // while(clear){
    //     console.log("antyhing happening")
    //     clear.addEventListener('click',clear_canvas)
    // }
    function changeColor(e){
        console.log(this)
        draw_color = this.style.background;
        console.log(draw_color)
    }
    for (const color of color_field) {
        console.log("inside for loop)")
        color.addEventListener('click', changeColor)
        
    }
    
    
    canvas.addEventListener("mousedown", start, false);
    canvas.addEventListener("mousemove", draw, false);

    canvas.addEventListener("mouseup", stop, false);
    canvas.addEventListener("mouseout", stop, false);

    function start(event){
        console.log("start")
        is_drawing = true;
        context.beginPath();
        context.moveTo(event.clientX - canvas.offsetLeft,
                        event.clientY - canvas.offsetTop);
        event.preventDefault();
    }

    function draw(event){
        console.log("drawing")
        console.log(draw_color)
        if( is_drawing ){
            context.lineTo(event.clientX - canvas.offsetLeft,
                            event.clientY - canvas.offsetTop);
            context.strokeStyle = draw_color;
            context.lineWidth = draw_width;
            context.lineCap = "round";
            context.lineJoin = "round";
            context.stroke();
        }   
        event.preventDefault();
    }

    function stop(event){
        console.log("stopping")
        if( is_drawing ){
            context.stroke();
            context.closePath();
            is_drawing = false;
        }
        event.preventDefault();
    }

});
