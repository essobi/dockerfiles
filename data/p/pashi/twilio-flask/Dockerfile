FROM pashi/uwsgi-flask  
MAINTAINER pasi@pashi.net  
# 20181602  
RUN apk add py-cffi py-enum34 py2-jwt py2-urllib3 py2-requests py2-openssl &&
pip install twilio  
ADD webapp /webapp/  
EXPOSE 8080  
CMD ["uwsgi", "/webapp/uwsgi.ini"]  
  

