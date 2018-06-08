FROM python:3  
MAINTAINER Alexey Sharapov "nekoth@gmail.com"  
RUN mkdir -p /app/web  
WORKDIR /app/web  
COPY requirements.txt /app/web/requirements.txt  
RUN pip install -r requirements.txt  
COPY . /app/web  
VOLUME ["/app/db"]  
EXPOSE 5000  
CMD python flask_test_2.py

