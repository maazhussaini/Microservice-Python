from groq import Groq

GROQ_KEY="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"

def analyze_code_with_llm(file_content, file_name):
    
    prompt = f"""
    Analyze the following code for:
        - Code style and formatting issues
        - Potential bugs or error
        - Performance Improvements
        - Best Practice
    File: {file_name}
    Content: {file_content}
    
    Provide a detailed JSON Output with the structure:
    ```
    {{
        "issues": [
            {{
                type" : "<style | bugs | performance | best practice>",
                "line": <line number>,
                "description" : "<description>",
                "suggestion": "<suggestion>"
            }}
        ]
    }}
    ```JSON
    """
    
    client = Groq(
        api_key=GROQ_KEY
    )
    completion = client.chat.completions.create(
        model= "llama3-8b-8192" ,
        messages= [
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature= 1,
        top_p = 1
    )
    
    print(completion.choices[0].message.content)
