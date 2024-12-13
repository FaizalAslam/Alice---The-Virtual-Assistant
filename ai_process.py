from openai import OpenAI


def aiProcess(command):
    client = OpenAI(api_key="")   #Please enter your API key to be able to use AI feature
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system", 
                "content": "You are a virtual assistant named alice. You respond to the user with accurate and brief answers."
            },
            {
                "role": "user",
                "content": command
            }
        ]
    )
    return (completion.choices[0].message.content)