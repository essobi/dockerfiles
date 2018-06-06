FROM python:2.7  
ADD requirements.txt /code/requirements.txt  
WORKDIR /codes  
RUN pip install -r requirements.txt  
ADD . /codes  
CMD ["python", "app.py"]  

