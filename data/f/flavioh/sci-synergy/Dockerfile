FROM python:alpine3.6  
ADD . /web/  
WORKDIR /web  
RUN pip install -r requirements.txt  
ENTRYPOINT ["python","app.py"]  

