from groq import Groq

GROQ_KEY="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"

content = "ZnJvbSBncm9xIGltcG9ydCBHcm9xCgpHUk9RX0tFWT0iWXZydXVEakhjc2p2MWhsbTJ3V3dXR2QxMjNkYXNkRllUQVZCU09MbnpjWDBOOFkwUlhpdWVyZWIiCgpkZWYgYW5hbHl6ZV9jb2RlX3dpdGhfbGxtKGZpbGVfY29udGVudCwgZmlsZV9uYW1lKToKICAgIAogICAgcHJvbXB0ID0gZiIiIgogICAgQW5hbHl6ZSB0aGUgZm9sbG93aW5nIGNvZGUgZm9yOgogICAgICAgIC0gQ29kZSBzdHlsZSBhbmQgZm9ybWF0dGluZyBpc3N1ZXMKICAgICAgICAtIFBvdGVudGlhbCBidWdzIG9yIGVycm9yCiAgICAgICAgLSBQZXJmb3JtYW5jZSBJbXByb3ZlbWVudHMKICAgICAgICAtIEJlc3QgUHJhY3RpY2UKICAgIEZpbGU6IHtmaWxlX25hbWV9CiAgICBDb250ZW50OiB7ZmlsZV9jb250ZW50fQogICAgCiAgICBQcm92aWRlIGEgZGV0YWlsZWQgSlNPTiBPdXRwdXQgd2l0aCB0aGUgc3RydWN0dXJlOgogICAgYGBgCiAgICB7ewogICAgICAgICJpc3N1ZXMiOiBbCiAgICAgICAgICAgIHt7CiAgICAgICAgICAgICAgICB0eXBlIiA6ICI8c3R5bGUgfCBidWdzIHwgcGVyZm9ybWFuY2UgfCBiZXN0IHByYWN0aWNlPiIsCiAgICAgICAgICAgICAgICAibGluZSI6IDxsaW5lIG51bWJlcj4sCiAgICAgICAgICAgICAgICAiZGVzY3JpcHRpb24iIDogIjxkZXNjcmlwdGlvbj4iLAogICAgICAgICAgICAgICAgInN1Z2dlc3Rpb24iOiAiPHN1Z2dlc3Rpb24+IgogICAgICAgICAgICB9fQogICAgICAgIF0KICAgIH19CiAgICBgYGBKU09OCiAgICAiIiIKICAgIAogICAgY2xpZW50ID0gR3JvcSgKICAgICAgICBhcGlfa2V5PUdST1FfS0VZCiAgICApCiAgICBjb21wbGV0aW9uID0gY2xpZW50LmNoYXQuY29tcGxldGlvbnMuY3JlYXRlKAogICAgICAgIG1vZGVsPSAibGxhbWEzLThiLTgxOTIiICwKICAgICAgICBtZXNzYWdlcz0gWwogICAgICAgICAgICB7CiAgICAgICAgICAgICAgICAicm9sZSI6ICJ1c2VyIiwKICAgICAgICAgICAgICAgICJjb250ZW50IjogcHJvbXB0CiAgICAgICAgICAgIH0KICAgICAgICBdCiAgICAgICAgdGVtcGVyYXR1cmU9IDEsCiAgICAgICAgdG9wX3AgPSAxCiAgICApCiAgICAKICAgIHByaW50KGNvbXBsZXRpb24uY2hvaWNlc1swXS5tZXNzYWdlLmNvbnRlbnQpCg=="

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
    

analyze_code_with_llm(content, "script.py")
