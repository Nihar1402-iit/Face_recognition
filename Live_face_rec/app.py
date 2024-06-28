#Imports and setup
import uuid ## random id generator
from streamlit_option_menu import option_menu
from settings import *
import logging
# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

## Disable Warnings
st.set_option('deprecation.showPyplotGlobalUse', False)
st.set_option('deprecation.showfileUploaderEncoding', False)
################################################### Defining Static Data ###############################################
st.sidebar.image('data:image/jpeg;base64,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',
                 use_column_width=False)
st.sidebar.markdown("""
                    > Made by [*Nihar Shah*](https://www.linkedin.com/in/nihar-shah-63162425a/)
                    """)

user_color      = '#000000'
title_webapp    = "Visitor Monitoring Webapp"
image_link      = "https://static.vecteezy.com/system/resources/previews/020/045/181/non_2x/verified-checkmark-sign-icon-symbol-logo-green-design-free-vector.jpg"

html_temp = f"""
            <div style="background-color:{user_color};padding:12px">
            <h1 style="color:white;text-align:center;">{title_webapp}
            <img src = "{image_link}" align="right" width=150px ></h1>
            </div>
            """
st.markdown(html_temp, unsafe_allow_html=True)

###################### Defining Static Paths ###################
# Button for Clearing Database
if st.sidebar.button('Click to Clear out all the data'):
    ## Clearing Visitor Database
    shutil.rmtree(VISITOR_DB, ignore_errors=True)
    os.mkdir(VISITOR_DB)
    ## Clearing Visitor History
    shutil.rmtree(VISITOR_HISTORY, ignore_errors=True)
    os.mkdir(VISITOR_HISTORY)

if not os.path.exists(VISITOR_DB):
    os.mkdir(VISITOR_DB)

if not os.path.exists(VISITOR_HISTORY):
    os.mkdir(VISITOR_HISTORY)
# st.write(VISITOR_HISTORY)
########################################################################################################################
def main():
    ###################################################
    st.sidebar.header("About")
    st.sidebar.info("This webapp gives a demo of Visitor Monitoring "
                    "Webapp using 'Face Recognition' and Streamlit")
    ###################################################

    selected_menu = option_menu(None,
        ['Visitor Validation', 'View Visitor History', 'Add to Database'],
        icons=['camera', "clock-history", 'person-plus'],
        ## icons from website: https://icons.getbootstrap.com/
        menu_icon="cast", default_index=0, orientation="horizontal")

    if selected_menu == 'Visitor Validation':
        ## Generates a Random ID for image storage
        visitor_id = uuid.uuid1()

        ## Reading Camera Image
        img_file_buffer = st.camera_input("Take a picture")

        if img_file_buffer is not None:
            bytes_data = img_file_buffer.getvalue()

            # convert image from opened file to np.array
            image_array         = cv2.imdecode(np.frombuffer(bytes_data,
                                                             np.uint8),
                                               cv2.IMREAD_COLOR)
            image_array_copy    = cv2.imdecode(np.frombuffer(bytes_data, np.uint8), cv2.IMREAD_COLOR)
            # st.image(cv2_img)

            ## Saving Visitor History
            with open(os.path.join(VISITOR_HISTORY,
                                   f'{visitor_id}.jpg'), 'wb') as file:
                file.write(img_file_buffer.getbuffer())
                st.success('Image Saved Successfully!')

                ## Validating Image
                # Detect faces in the loaded image
                max_faces   = 0
                rois        = []  # region of interests (arrays of face areas)

                ## To get location of Face from Image
                face_locations  = face_recognition.face_locations(image_array)
                ## To encode Image to numeric format
                encodesCurFrame = face_recognition.face_encodings(image_array,
                                                                  face_locations)

                ## Generating Rectangle Red box over the Image
                for idx, (top, right, bottom, left) in enumerate(face_locations):
                    # Save face's Region of Interest
                    rois.append(image_array[top:bottom, left:right].copy())

                    # Draw a box around the face and label it
                    cv2.rectangle(image_array, (left, top), (right, bottom), COLOR_DARK, 2)
                    cv2.rectangle(image_array, (left, bottom + 35), (right, bottom), COLOR_DARK, cv2.FILLED)
                    font = cv2.FONT_HERSHEY_DUPLEX
                    cv2.putText(image_array, f"#{idx}", (left + 5, bottom + 25), font, .55, COLOR_WHITE, 1)

                ## Showing Image
                st.image(BGR_to_RGB(image_array), width=720)

                ## Number of Faces identified
                max_faces = len(face_locations)

                if max_faces > 0:
                    col1, col2 = st.columns(2)

                    # select selected faces in the picture
                    face_idxs = col1.multiselect("Select face#", range(max_faces),
                                                 default=range(max_faces))

                    ## Filtering for similarity beyond threshold
                    similarity_threshold = col2.slider('Select Threshold for Similarity',
                                                         min_value=0.0, max_value=1.0,
                                                         value=0.5)
                                                    ## check for similarity confidence greater than this threshold

                    flag_show = False

                    if ((col1.checkbox('Click to proceed!')) & (len(face_idxs)>0)):
                        dataframe_new = pd.DataFrame()

                        ## Iterating faces one by one
                        for face_idx in face_idxs:
                            ## Getting Region of Interest for that Face
                            roi = rois[face_idx]
                            # st.image(BGR_to_RGB(roi), width=min(roi.shape[0], 300))

                            # initial database for known faces
                            database_data = initialize_data()
                            # st.write(DB)

                            ## Getting Available information from Database
                            face_encodings  = database_data[COLS_ENCODE].values
                            dataframe       = database_data[COLS_INFO]

                            # Comparing ROI to the faces available in database and finding distances and similarities
                            faces = face_recognition.face_encodings(roi)
                            # st.write(faces)

                            if len(faces) < 1:
                                ## Face could not be processed
                                st.error(f'Please Try Again for face#{face_idx}!')
                            else:
                                face_to_compare = faces[0]
                                ## Comparing Face with available information from database
                                dataframe['distance'] = face_recognition.face_distance(face_encodings,
                                                                                       face_to_compare)
                                dataframe['distance'] = dataframe['distance'].astype(float)

                                dataframe['similarity'] = dataframe.distance.apply(
                                    lambda distance: f"{face_distance_to_conf(distance):0.2}")
                                dataframe['similarity'] = dataframe['similarity'].astype(float)

                                dataframe_new = dataframe.drop_duplicates(keep='first')
                                dataframe_new.reset_index(drop=True, inplace=True)
                                dataframe_new.sort_values(by="similarity", ascending=True)

                                dataframe_new = dataframe_new[dataframe_new['similarity'] > similarity_threshold].head(1)
                                dataframe_new.reset_index(drop=True, inplace=True)

                                if dataframe_new.shape[0]>0:
                                    (top, right, bottom, left) = (face_locations[face_idx])

                                    ## Save Face Region of Interest information to the list
                                    rois.append(image_array_copy[top:bottom, left:right].copy())

                                    # Draw a Rectangle Red box around the face and label it
                                    cv2.rectangle(image_array_copy, (left, top), (right, bottom), COLOR_DARK, 2)
                                    cv2.rectangle(image_array_copy, (left, bottom + 35), (right, bottom), COLOR_DARK, cv2.FILLED)
                                    font = cv2.FONT_HERSHEY_DUPLEX
                                    cv2.putText(image_array_copy, f"#{dataframe_new.loc[0, 'Name']}", (left + 5, bottom + 25), font, .55, COLOR_WHITE, 1)

                                    ## Getting Name of Visitor
                                    name_visitor = dataframe_new.loc[0, 'Name']
                                    attendance(visitor_id, name_visitor)

                                    flag_show = True

                                else:
                                    st.error(f'No Match Found for the given Similarity Threshold! for face#{face_idx}')
                                    st.info('Please Update the database for a new person or click again!')
                                    attendance(visitor_id, 'Unknown')

                        if flag_show == True:
                            st.image(BGR_to_RGB(image_array_copy), width=720)

                else:
                    st.error('No human face detected.')

    if selected_menu == 'View Visitor History':
        view_attendace()

    if selected_menu == 'Add to Database':
        col1, col2, col3 = st.columns(3)

        face_name  = col1.text_input('Name:', '')
        pic_option = col2.radio('Upload Picture',
                                options=["Upload a Picture",
                                         "Click a picture"])

        if pic_option == 'Upload a Picture':
            img_file_buffer = col3.file_uploader('Upload a Picture',
                                                 type=allowed_image_type)
            if img_file_buffer is not None:
                # To read image file buffer with OpenCV:
                file_bytes = np.asarray(bytearray(img_file_buffer.read()),
                                        dtype=np.uint8)

        elif pic_option == 'Click a picture':
            img_file_buffer = col3.camera_input("Click a picture")
            if img_file_buffer is not None:
                # To read image file buffer with OpenCV:
                file_bytes = np.frombuffer(img_file_buffer.getvalue(),
                                           np.uint8)

        if ((img_file_buffer is not None) & (len(face_name) > 1) &
                st.button('Click to Save!')):
            # convert image from opened file to np.array
            image_array = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
            # st.write(image_array)
            # st.image(cv2_img)

            with open(os.path.join(VISITOR_DB,
                                   f'{face_name}.jpg'), 'wb') as file:
                file.write(img_file_buffer.getbuffer())
                # st.success('Image Saved Successfully!')

            face_locations = face_recognition.face_locations(image_array)
            encodesCurFrame = face_recognition.face_encodings(image_array,
                                                              face_locations)

            df_new = pd.DataFrame(data=encodesCurFrame,
                                  columns=COLS_ENCODE)
            df_new[COLS_INFO] = face_name
            df_new = df_new[COLS_INFO + COLS_ENCODE].copy()

            # st.write(df_new)
            # initial database for known faces
            DB = initialize_data()
            add_data_db(df_new)

#######################################################
if __name__ == "__main__":
    main()
#######################################################

