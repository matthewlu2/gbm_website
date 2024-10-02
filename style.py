import streamlit as st

footer="""
<style>
  
    .image 
    { 
        padding: 10px;
        transition: transform .2s;
    }


    .image:hover {  
        transform: scale(1.5);
        transition: 0.2s;
    }
    
    .footer {
        position: relative;
        width: 100%;
        left: 0;
        bottom: 0;
        background-color: white;
        margin-top: auto;
        color: black;
        padding: 24px;
        text-align: center;
    }
</style>

<div class="footer">
<p style="font-size:  13px">© 2024 Osmanbeyoglulab.com. All rights reserved.</p>
<a href="https://hillman.upmc.com/"><img class="image" src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS7c7pXIkFgMPVM2csVE6MenUFLEsgF5beCeMJzogkPkXPC4xEo9OTHf6nVpqsb3PvisRk&usqp=CAU"alt="github" width="70" height=50"></a>
<a href="https://www.pitt.edu/"><img class="image" src="https://upload.wikimedia.org/wikipedia/en/thumb/f/fb/University_of_Pittsburgh_seal.svg/300px-University_of_Pittsburgh_seal.svg.png"alt="github" width="45" height="45"></a>
<a href="https://github.com/osmanbeyoglulab"><img class="image" src="https://cdn-icons-png.flaticon.com/512/25/25231.png" alt="github" width="45" height="45"></a>
<a href="https://scholar.google.com/citations?user=YzCsmdgAAAAJ&hl=en&inst=7044483460239389945"><img class="image" src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c7/Google_Scholar_logo.svg/512px-Google_Scholar_logo.svg.png"alt="github" width="45" height="45"></a>
</div>

"""


page_style = """
    <style>
        #MainMenu {visibility: hidden;} 
        footer {visibility: hidden;} 
    </style>
"""
