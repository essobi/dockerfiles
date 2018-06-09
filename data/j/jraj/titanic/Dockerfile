#FROM tiangolo/uwsgi-nginx-flask:flask  
FROM tiangolo/uwsgi-nginx-flask:flask-python3.5  
COPY ./requirements.txt /requirements.txt  
RUN pip install -r /requirements.txt  
COPY ./app /app  

