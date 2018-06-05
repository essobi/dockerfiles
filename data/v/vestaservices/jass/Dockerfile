FROM python:3.6-alpine  
MAINTAINER anton.zakharov@crim.ca  
  
# need bash  
RUN apk add --update bash && rm -rf /var/cache/apk/*  
  
RUN pip3 install gunicorn  
  
ENV JASS_CONFIG_PATH "/opt/jass_deploy/config.ini"  
ENV JASS_VERSION 1.1.10  
RUN mkdir -p /opt/jass_deploy  
  
COPY . /opt/jass_deploy  
RUN cd /opt/jass_deploy && pip install -e .  
  
RUN chmod +x /opt/jass_deploy/jass_startup.sh  
  
EXPOSE 5000  
WORKDIR /opt/jass_deploy  
CMD ["./jass_startup.sh"]  

