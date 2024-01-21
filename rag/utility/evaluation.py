from ragas import evaluate
from ragas.metrics import (faithfulness, answer_relevancy, context_recall, context_precision,)
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.schema.runnable import RunnablePassthrough
from langchain.schema.output_parser import StrOutputParser


def generator(retriever, template):
    # Define LLM
    llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)

    # Define prompt template
    template =template
    prompt = ChatPromptTemplate.from_template(template)

    # Setup RAG pipeline
    rag_chain = (
        {"context": retriever,  "question": RunnablePassthrough()} 
        | prompt 
        | llm
        | StrOutputParser() 
    )
    return rag_chain

def data_generation(prompt, retriever, questions, ground_truths):

    answers = []
    contexts = []
    rag_chain = generator(retriever, prompt)
    # Inference
    for query in questions:

        answers.append(rag_chain.invoke(query))
        contexts.append([docs.page_content for docs in retriever.get_relevant_documents(query)])

    # To dict
    data = {
        "question": questions, # list 
        "answer": answers, # list
        "contexts": contexts, # list list
        "ground_truths": ground_truths # list Lists
    }

    # Convert dict to dataset
    # dataset = Dataset.from_dict(data)

    return data

def evaluation(dataset):
   
    result = evaluate(
    dataset = dataset, 
    metrics=[
        context_precision,
        context_recall,
        faithfulness,
        answer_relevancy,
    ],
    )

    df = result.to_pandas()
    return df