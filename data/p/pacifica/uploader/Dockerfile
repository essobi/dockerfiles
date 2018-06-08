FROM python:2-onbuild  
MAINTAINER david.brown@pnnl.gov  
  
RUN apt-get update && apt-get -y install expect && apt-get clean all  
RUN rm -f /usr/src/app/home/UploaderConfig.json
/usr/src/app/UploaderConfig.json && ln -sf /srv/UploaderConfig.json
/usr/src/app/UploaderConfig.json  
ENV PYTHONPATH /usr/src/app  
RUN python manage.py migrate  
RUN chmod +x ./setup-superuser  
RUN ./setup-superuser  
RUN chown -R 1:1 -R /usr/src/app  
RUN chmod og+rwx -R /usr/src/app  

