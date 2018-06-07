FROM python:3.5  
RUN mkdir /app  
  
COPY alice /app/alice  
COPY gunicorn /app/gunicorn  
COPY ui /app/ui  
COPY users /app/users  
COPY wins /app/wins  
  
COPY requirements.txt /app/requirements.txt  
COPY manage.py /app/manage.py  
COPY start.sh /app/start.sh  
  
WORKDIR /app  
RUN pip install -r requirements.txt  
  
EXPOSE 8001  
CMD ./start.sh

