FROM python:3.5  
ADD . /app/  
WORKDIR /app/  
RUN pip install -r requirements.txt  
WORKDIR /app/timemachine/  
RUN python manage.py collectstatic --no-input  
CMD python manage.py runserver 0.0.0.0:80  

