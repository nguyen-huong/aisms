import openai
openai.api_key = "sk-proj-secrets"

# Define the prompt to review and optimize ISMS compliance with NIST 800-53, 800-30, and ISO standards
prompt = f"""
    I have an Information Security Management System (ISMS) section that needs to be reviewed \
    and optimized for compliance with NIST 800-53, NIST 800-30, and ISO standards. \
    Please assess the current ISMS, identify any gaps or areas for improvement, \
    and provide recommendations to enhance compliance. Focus on:
    
    - Aligning security and privacy controls with NIST 800-53 requirements.
    - Ensuring the ISMS risk management framework aligns with NIST 800-30.
    - Adhering to ISO controls, particularly in governance, asset management, \
    human resources, and continuous improvement.
    
    ### Here is the ISMS section in MD:
    {isms_description}
    
    ### Here is the NIST/ISO standards I want to look at:
    NIST 800-53: https://csrc.nist.gov/publications/detail/sp/800-53/rev-5/final
    NIST 800-30: https://csrc.nist.gov/publications/detail/sp/800-30/rev-1/final
    {nist_800_30_description}

"""
# Generate the optimized ISMS description using OpenAI's GPT-3.5-turbo model
response = openai.Completion.create(
    engine="text-davinci-003",
    prompt=prompt,

    max_tokens=1000,
    n=1
    stop=None,
    temperature=0.7)


isms_description = """
    The Information Security Management System (ISMS) is a comprehensive framework designed to ensure the confidentiality, integrity, and availability of information assets. It encompasses policies, procedures, and controls to manage risks and ensure compliance with relevant standards and regulations.
    """
nist_800_30_description = """
    NIST 800-30 is a risk management framework that provides guidance on how to identify, assess, and manage risks to organizational operations, assets, individuals, other organizations, and the nation.
    """
iso_description = """
    ISO 27001 is an international standard that provides a framework for implementing an ISMS. It outlines the requirements for establishing, implementing, maintaining, and continually improving the ISMS.
    """

# api call
response = openai.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": prompt}
    ], 
    temperature = 0.25
)

isms = response.choices[0].message.content
