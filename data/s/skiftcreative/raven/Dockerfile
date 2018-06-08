# nginx-gunicorn-flask  
FROM skiftcreative/supervisor:latest  
MAINTAINER Shawn McElroy <shawn@skift.io>  
  
ENV SLACK_TOKEN "xoxb..."  
COPY . /deploy  
WORKDIR /deploy  
  
RUN pip install -U pip  
  
RUN pip install -r /deploy/requirements.txt \  
&& python setup.py install  
  
COPY docker/supervisord.conf /etc/supervisor/conf.d/supervisord.conf  

