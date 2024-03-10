import streamlit as st


def entered_cred():
    if 'user' in st.session_state and 'pwd' in st.session_state:
        if st.session_state['user'].strip() == 'admin' and st.session_state['pwd'].strip() == 'admin':
            st.session_state['authenticated'] = True
        else:
            st.session_state['authenticated'] = False
            if not st.session_state['pwd']:
                st.warning('please enter password')
            elif not st.session_state['user']:
                st.warning('please enter username')
            else:
                st.error('Invalid Username/Password :face_with_raised_eyebrow')

        print(f"authenticated: {st.session_state['authenticated']}")

def authenticate_user():
    if 'authenticated' not in st.session_state:
        st.session_state['user'] = ''
        st.session_state['pwd'] = ''
        st.text_input(label='username :', value='', key='user', on_change=entered_cred)
        st.text_input(label='password :', value='', key='pwd', type='password', on_change=entered_cred)
        return False
    else:
        if st.session_state['authenticated']:
            return True
        else:
            st.text_input(label='username :', value='', key='user', on_change=entered_cred)
            st.text_input(label='password :', value='', key='pwd', type='password', on_change=entered_cred)
            return False

if __name__ == '__main__':
    authenticate_user()
