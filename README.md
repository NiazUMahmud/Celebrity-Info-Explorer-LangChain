# Celebrity Info Explorer

This Streamlit application allows you to search for information about celebrities using the power of OpenAI's language models. It provides a quick and easy way to get insights into a celebrity's background, date of birth, and significant events surrounding that time.
![image](https://github.com/user-attachments/assets/5a449777-6ccb-4bb7-a2b9-6aa1d2ac2a57)
![image](https://github.com/user-attachments/assets/b00c1a6d-b048-454e-bfde-f23625de0844)
![image](https://github.com/user-attachments/assets/49816d5b-fd8e-4bc2-b04f-31fe03aa3aec)



https://github.com/user-attachments/assets/bf595451-15a5-4e4a-9798-f669757cd9d3


## Features

*   **Interactive Search:** Simply enter a celebrity's name, and the application will retrieve information using OpenAI.
*   **Detailed Output:** The results include a brief biography, the celebrity's date of birth, and a list of notable world events around the time of their birth.
*   **Clean UI:** The application is built with a focus on a modern and easy-to-use interface using Streamlit, enhanced with custom CSS for a professional look.
*   **Historical Context:** Explore major world events related to the celebrity's birth date to give a better perspective.
*   **Memory Tracking:** The application keeps track of the conversation history for each information category, which can be viewed in expandable sections for debug purposes.

## How to Use

1.  **Clone the Repository:**
    ```bash
    git clone <repository-url>
    ```
    *Replace `<repository-url>` with the actual URL of your Git repository.*

2.  **Install Dependencies:**
    Navigate into the cloned repository and install the required Python packages:
    ```bash
    pip install -r requirements.txt
    ```

    **Note:** Make sure you have a `requirements.txt` file in your repository listing the necessary packages (e.g., `streamlit`, `langchain`, `openai`, etc.). Example `requirements.txt` below

    ```
     openai
     langchain
     streamlit
    ```

3.  **Set Up OpenAI API Key:**
    *   Create a `constants.py` file or similar in the main directory of your app
    *   In `constants.py` set the API key as `openai_key = "YOUR_OPENAI_API_KEY"`. Remember to replace `YOUR_OPENAI_API_KEY` with your actual OpenAI API key.
        **Note**:  Make sure not to include this file in git to avoid API key leak.

4.  **Run the Streamlit App:**
    ```bash
    streamlit run celebrity_app.py
    ```
    *This will launch the app in your default browser. The app name may differ, so change it to your file name*

5.  **Start Exploring:**
    *   Enter a celebrity's name in the text input field.
    *   Click or tap anywhere outside the input to submit your search.
    *   View the detailed results displayed below the search input.
    *   Expand the memory sections to see the raw history if needed.

## Code Overview

The application uses the following structure:

*   `constants.py` or similar : Stores the OpenAI API key. *Remember to remove this from Git.*
*   `celebrity_app.py`: The main Streamlit application file containing all the code for the UI and interaction with the language models.
*  `requirements.txt`: List of all the packages used by this application.
*   **Key Libraries Used:**
    *   `streamlit`: For building the web interface.
    *   `langchain`: For handling the interaction with language models and the creation of the memory buffer.
    *   `openai`: For accessing the OpenAI API.

## Contributing

Contributions are welcome! If you find any issues or have ideas for new features, feel free to submit a pull request.

1.  Fork the repository
2.  Create a new branch
3.  Make your changes
4.  Submit a pull request

## License

[Optional: Add a license if applicable, e.g., MIT License]

## Contact

[niazstatcu@gmail.com]
