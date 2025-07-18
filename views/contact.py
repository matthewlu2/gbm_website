import streamlit as st
 
st.markdown("<h2 style='text-align: center; color: black;'>Contact Us</h1>", unsafe_allow_html=True)  
st.write("")

st.markdown("<h3 style='text-align: center; color: black; font-size:25px;'>The Department of Biomedical Informatics (DBMI) </h3>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: black; font-size:25px;'>University of Pittsburgh School of Medicine</h3>", unsafe_allow_html=True)

st.markdown("""<div style="width: 100%"><iframe width="100%" height="500" frameborder="0" scrolling="no" marginheight="0" marginwidth="0" src="https://maps.google.com/maps?width=100%25&amp;height=600&amp;hl=en&amp;q=5051%20Centre%20Avenue%20Pittsburgh,%20PA%2015213+(My%20Business%20Name)&amp;t=p&amp;z=14&amp;ie=UTF8&amp;iwloc=B&amp;output=embed"><a href="https://www.maps.ie/distance-area-calculator.html">measure distance on map</a></iframe></div>""", unsafe_allow_html=True)
st.write("")

b, c = st.columns([ .7, .0001])
st.markdown('##### If you have any questions or feedback, please feel free to contact us:')
a2, b2, _ = st.columns([ .25, .25, .1])
a2.markdown("""<span style="font-size:18px;">Hatice Osmanbeyoglu<br>Principal Investigator<br>✉️ osmanbeyogluhu@pitt.edu</span>""", unsafe_allow_html=True)
a2.markdown("""<span style="font-size:18px;">Linan Zhang<br>Assistant Professor<br>✉️ liz133@pitt.edu</span>""", unsafe_allow_html=True)
b2.markdown("""<span style="font-size:18px;">Matthew Lu<br>Undergraduate Researcher<br>✉️ mal554@pitt.edu</span>""", unsafe_allow_html=True)
b2.markdown("""<span style="font-size:18px;">Xiaojun Ma<br>Software Engineer<br>✉️ xim33@pitt.edu</span>""", unsafe_allow_html=True)
   
