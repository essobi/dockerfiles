FROM python:3  
EXPOSE 8000  
COPY . /usr/src/app  
WORKDIR /usr/src/app  
  
RUN pip install -r requirements.txt  
RUN pip install gunicorn  
  
RUN python3 manage.py migrate  
  
CMD gunicorn CONFER.wsgi -b 0.0.0.0:8000  

