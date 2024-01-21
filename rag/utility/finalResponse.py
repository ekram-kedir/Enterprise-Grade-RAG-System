import os,sys
import json
from datasets import Dataset

rpath = os.path.abspath('./..')
if rpath not in sys.path:
    sys.path.insert(0, rpath)

from .evaluation import generator,evaluation, data_generation
from .loader import data_loader
from .retriever import create_retriever


def readfile(file_path:str):
   # Open the file in read mode
    with open(file_path, 'r') as file:
    # Read the contents of the file
        file_contents = file.read()
    return file_contents

def generalResponse(question):
    chunks =  data_loader(file_path="../../rag/prompts/challenge_document.txt")
    retriever = create_retriever(chunks)
    file_contents = readfile(file_path='../../rag/prompts/generate_prompt.txt')
    rag_chain = generator(retriever= retriever ,template=file_contents)
    generated_prompts = rag_chain.invoke(question)
    print(generated_prompts)
    generated = json.loads(generated_prompts)
    prompts = [item['prompt'] for item in generated]
    ground_truths = [item['ground_truth'].split(', ') for item in generated]
    answer = data_generation(prompt=file_contents,retriever=retriever, questions=prompts, ground_truths=ground_truths)
    answer = Dataset.from_dict(answer)
    response = evaluation(answer)

    return response