# import namespaces
from azure.core.credentials import AzureKeyCredential
from azure.ai.language.questionanswering import QuestionAnsweringClient

# Create client using endpoint and key
credential = AzureKeyCredential(ai_key)
ai_client = QuestionAnsweringClient(endpoint=ai_endpoint, credential=credential)

# Submit a question and display the answer
user_question = ''
while user_question.lower() != 'quit':
    user_question = input('\nQuestion:\n')
    response = ai_client.get_answers(question=user_question,
                                    project_name=ai_project_name,
                                    deployment_name=ai_deployment_name)
    for candidate in response.answers:
        print(candidate.answer)
        print("Confidence: {}".format(candidate.confidence))
        print("Source: {}".format(candidate.source))
