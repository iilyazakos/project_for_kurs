import rsa
import streamlit as st



(pubkey, privkey) = rsa.newkeys(512)
st.set_page_config(layout = "wide")
st.title('Шифрование методом RSA')
with st.container() as ininput:
    word = st.text_input("Введите слово для дальнейшей его шифрации")
    crypto = rsa.encrypt(word.encode('utf8'), pubkey)  # Encryption

with st.container() as out_code:
    if word!=(''):
        st.write('Закодированное слово:')
        st.write(str(crypto))

with st.container() as decode:
    st.write('Декодированное слово:')
    message = rsa.decrypt(crypto, privkey)  # Decryption
    st.write(message.decode('utf8'))

with st.container() as download_priv:
    st.download_button('Скачать открытый ключ', str(pubkey), file_name = 'Public key.txt')
