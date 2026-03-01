from llm_helper import llm
from few_shot import FewShotPosts

few_shot = FewShotPosts()

def get_length_str(length):
    if length =="Short":
        return "1 to 8 lines"
    if length=="Medium":
        return "8 to 12 lines"
    if length =="Long":
        return "12 to 18 lines"

def get_prompt(length, language, tag, tone):
    length_str = get_length_str(length)
    prompt = f'''
    Generate a LinkedIn post using the below information. No preamble.

    1) Topic: {tag}
    2) Length: {length}
    3) Language: {language}
    4) Tone: {tone}

    If Language is Hinglish then it means it is a mix of Hindi and English.
    The final script of the post should always be English.
    '''
    examples = few_shot.get_filtered_posts(length, language, tag)
    
    if len(examples)>=0:
        prompt += "4) Use the writing style as per the following examples."
        for i, post in enumerate(examples):
            post_text = post['text']
            prompt += f"\n\n Example {i+1}: \n\n {post_text}"

            if i==1:
                break
    return prompt

def generate_post(length, language, tag, tone):
    prompt = get_prompt(length, language, tag, tone)
    response = llm.invoke(prompt)
    return response.content

def generate_hashtags(text):
    prompt = f"""
    Generate 5 professional LinkedIn hashtags for the following post.
    Return only hashtags, comma-separated. No preamble.

    Post: {text}
    """
    response = llm.invoke(prompt)
    return response.content.strip()


if __name__ =="__main__":
    post = generate_post("Short", "English", "Education", "Motivational")
    print(post)