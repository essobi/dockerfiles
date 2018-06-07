FROM alpine:latest  
  
COPY application/ /application  
  
WORKDIR /application  
  
RUN apk update \  
&& apk add python \  
py-gunicorn \  
py-pip \  
py-psycopg2 \  
&& pip install -r trackapp/requirements.txt  
  
EXPOSE 5000  
CMD gunicorn -b 0.0.0.0:5000 wsgi:app  

