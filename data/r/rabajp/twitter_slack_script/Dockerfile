FROM python:3.6.2-alpine  
LABEL maintainer "Hiroki Sakuraba <sakuraba@tech.gr.jp>"  
  
RUN mkdir /app  
WORKDIR /app  
ADD . /app  
RUN pip install -r requirements.txt  
  
CMD ["python", "run.py"]  

