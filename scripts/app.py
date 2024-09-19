import streamlit as st
import google.generativeai as genai

def get_story_from_prompt(story_prompt, model):
    """
    Calls the LLM with the provided story prompt to generate a story.

    Args:
        story_prompt (str): The prompt describing the story requirements.
        model: The generative model object to call.

    Returns:
        str: The generated story content.
    """
    prompt = f"""
Generate a comprehensive story based on the provided story prompt. Your task is to:
### Provided Information:
1. **story_prompt **: {story_prompt}
structure story like:
Name of story
intro to characters and professions (all will be hypothetical)
story 
moral of story
do you like ? ask for more !
The ABDCE structure is a great way to outline a short story. 
It stands for Action, Background, Development, Climax, and Ending. 
By following this simple formula, you can ensure that your story has a strong beginning, middle, and end that keeps your readers hooked from the first to the last page.
1. Create a cohesive and engaging narrative that fits the provided context.
2. Include detailed descriptions, character developments, and plot progressions as appropriate to the story prompt.
3. Enhance clarity and add creative elements to make the story captivating.
4. add proper words of expression like omgggg, woowwwww , hushhhhh, like wise, but not limited to, which are senario specific.
5. create characters and good names to that. check for things which will put user intact with story.
6. check if you can use any quote or slang (with credits) if relevent 
5. at end of story, people should feel amazed or good"""

    # Call to the language model API
    response = model.generate_content(prompt)
    response_content = response  # Adjust based on actual response structure
    return response_content.text


def save_story_to_file(story_text, output_file_path):
    """
    Saves the generated story text to a file.

    Args:
        story_text (str): The text content of the generated story.
        output_file_path (str): The path where the file should be saved.
    """
    with open(output_file_path, 'w', encoding='utf-8') as file:
        file.write(story_text)

# Streamlit app
def main():
    st.title("Story Generator with Google Generative AI")

    # Input: API key from the user
    api_key = st.text_input("Enter your API key", type="password")

    if api_key:
        # Configure the Generative AI model with the user-provided API key
        try:
            genai.configure(api_key=api_key)
            model = genai.GenerativeModel('gemini-1.5-flash-001')

            # Input: Story prompt from the user
            story_prompt = st.text_input("Enter the topic or theme for the story:")
            
            # Button to generate the story
            if st.button("Generate Story"):
                if story_prompt:
                    # Generate the story based on the provided prompt
                    story_text = get_story_from_prompt(story_prompt, model)

                    # Display the generated story
                    st.subheader("Generated Story")
                    st.write(story_text)

                    # Provide a download button to save the generated story
                    output_file_path = "Generated_Story.txt"
                    save_story_to_file(story_text, output_file_path)
                    st.success(f"Generated story saved to {output_file_path}")
                    st.download_button(
                        label="Download Story",
                        data=story_text,
                        file_name="Generated_Story.txt",
                        mime="text/plain"
                    )
                else:
                    st.warning("Please enter a topic or theme for the story.")
        except Exception as e:
            st.error(f"Error: {e}")
    else:
        st.warning("Please enter your API key to proceed.")

if __name__ == "__main__":
    main()
