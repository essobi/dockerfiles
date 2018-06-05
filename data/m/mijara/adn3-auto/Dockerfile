FROM python:3  
ENV PYTHONUNBUFFERED 1  
EXPOSE 8000  
COPY . /src  
  
RUN pip install -r /src/requirements.txt  
  
WORKDIR /src  

