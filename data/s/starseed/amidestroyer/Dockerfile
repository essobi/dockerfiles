FROM python:3.6.2-stretch  
  
RUN mkdir -p /code  
  
ENV PYTHONPATH=/code  
  
ADD . /code  
  
WORKDIR /code  
  
RUN pip install -r requirements.txt  
  
ENTRYPOINT ["python3"]  
  

