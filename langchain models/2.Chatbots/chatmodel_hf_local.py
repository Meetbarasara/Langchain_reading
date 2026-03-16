from langchain_huggingface import HuggingFacePipeline , ChatHuggingFace

llm=HuggingFacePipeline.from_model_id(  
        model_id=="meta-llama/Meta-Llama-3-8B-Instruct",
        task="text-generation",
        pipeline_kwargs=dict(
          temperature=0.5,
          max_new_tokens=100
        )
    )
model = ChatHuggingFace(llm=llm)

responce= model.invoke("What is the capital of India?")
print(responce.content)

