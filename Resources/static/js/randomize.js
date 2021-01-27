function randomize(){
    d3.json("/get_quote").then(result=>{
        d3.select("#quote").html(result)
    })
    }
