import streamlit as st

st.title('Demo Project')
col1,col2 = st.columns(2)

with col1:
    st.image('llama.jpg')
with col2:
    st.write("""
    Llamas, native to the Andean highlands of South America, are captivating creatures that have seamlessly integrated into various human activities. Known for their resilience and amiable nature, llamas serve as reliable pack animals, carrying loads across challenging terrains. With a distinctive appearance, their elongated necks, large expressive eyes, and soft, luxurious coats make them endearing companions. Beyond their charming exterior, llamas are intelligent and responsive, easily trainable for tasks like guarding livestock. The fibers from their coats, prized for their softness and warmth, contribute to textiles. Llamas embody a harmonious blend of utility, companionship, and cultural significance.
    """)

st.subheader('The page ends here')
st.image('llama_wide.jpg')
