FROM deanchrisarmada/django-image-sample:latest  
# FROM python:2.7  
WORKDIR /usr/src/app  
COPY . .  
RUN pip install -r requirements.txt  
RUN django-admin startproject project .; exit 0  
# RUN timeout 20 yes | python manage.py makemigrations  
EXPOSE 8000:8000  
CMD supervisord -c supervisord.conf --nodaemon  
# CMD ping google.com  
# docker run -d -v $(pwd):/usr/src/app -p 8000:8000 deanchrisarmada/django-
image-sample:latest

