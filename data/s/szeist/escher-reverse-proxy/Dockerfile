FROM python:3.6  
RUN mkdir -p /app  
WORKDIR /app  
  
ADD requirements.txt /app  
RUN pip install -r requirements.txt && rm requirements.txt  
  
ADD . /app  
CMD python app.py

