from python:alpine3.6  
WORKDIR /app  
  
COPY requirements.txt .  
RUN pip3 install -U -r requirements.txt  
  
COPY do-spaces-tool.py .  
  
ENTRYPOINT ["python3", "do-spaces-tool.py"]  

