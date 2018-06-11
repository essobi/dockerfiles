FROM ubuntu:16.04  
RUN apt-get update -y  
RUN apt-get install -y python3-pip python-dev build-essential  
RUN yes | apt-get install gunicorn3  
  
COPY . /wealth-watcher  
WORKDIR /wealth-watcher  
  
RUN pip3 install -r requirements.txt  
RUN python3 manage.py makemigrations  
RUN python3 manage.py migrate  
ENTRYPOINT ["gunicorn3"]  
CMD ["--bind", "0.0.0.0:8000", "wealthwatcher.wsgi:application"]  
#ENTRYPOINT ["python3"]  
#CMD ["manage.py", "runserver"]  

