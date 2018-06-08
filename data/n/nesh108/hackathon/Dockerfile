FROM python:2.7  
RUN pip install --upgrade pip  
  
RUN mkdir /app  
WORKDIR /app  
  
EXPOSE 8080  
COPY requirements.txt /app  
RUN pip install -r requirements.txt  
  
COPY /georate /app/georate  

