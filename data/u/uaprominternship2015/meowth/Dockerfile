FROM ubuntu  
  
ENV LC_CTYPE C.UTF-8  
ENV APP_SETTINGS config.ProductionConfig  
ENV STATIC_DIST /staticdata/dist  
  
RUN apt-get update  
  
RUN apt-get install -y git python3-pip python3 libpq-dev npm \  
libjpeg-dev libfreetype6-dev zlib1g-dev libpng12-dev  
  
WORKDIR /hrportal  
RUN pip3 install -r requirements.txt  
RUN python3 manage.py collectstatic  
  
CMD gunicorn project:app --log-file=- -b 0.0.0.0:8000

