FROM pjango/base:3.5  
MAINTAINER Pjango <info@pjango.com>  
  
RUN apk update && apk upgrade  
  
RUN apk add --no-cache alpine-sdk libxml2-dev libxslt-dev libffi-dev
postgresql-dev  
  
COPY . /home/pjango/app  
  
COPY resources/conf/supervisor/supervisord.conf
/etc/supervisor/supervisord.conf  
  
COPY resources/conf/supervisor/pjangoapp.conf
/etc/supervisor/conf.d/pjangoapp.conf  
  
RUN pip install -r /home/pjango/app/resources/requirements/prod.txt  
  
VOLUME ["/home/pjango/app"]  
  
WORKDIR /home/pjango/app  
  
EXPOSE 8000  
CMD ["supervisord", "-n"]  

