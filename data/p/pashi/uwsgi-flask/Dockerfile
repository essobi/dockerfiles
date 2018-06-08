FROM alpine:latest  
MAINTAINER pasi@pashi.net  
# 20181602  
RUN mkdir -p /webapp/ && apk add --update py2-flask py2-pip uwsgi uwsgi-python
&& pip install flask-restful && pip install flask-cors  
ADD webapp /webapp/  
EXPOSE 8080  
EXPOSE 8001  
CMD ["uwsgi", "/webapp/uwsgi.ini"]  
  

