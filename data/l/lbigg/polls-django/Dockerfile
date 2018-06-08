FROM python:3.5-alpine  
RUN mkdir -p /django/static  
WORKDIR /django  
COPY ./mysite .  
RUN pip3 install -r requirements.txt  
RUN python3 manage.py makemigrations && \  
python3 manage.py migrate && \  
python3 manage.py collectstatic --noinput  
EXPOSE 8000  
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]  

