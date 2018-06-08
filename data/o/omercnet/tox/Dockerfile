FROM ubuntu  
MAINTAINER Omer Cohen <docker+tox@omer.io>  
  
RUN DEBIAN_FRONTEND=noninteractive apt-get update && \  
apt-get install -y python-pip python3-pip git && \  
python2 -m pip install -U pip tox tox-travis && \  
python3 -m pip install -U pip tox tox-travis  
  
WORKDIR /app  
VOLUME /app  
  
COPY docker-entrypoint.sh /docker-entrypoint.sh  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
ENV CMD tox  
CMD ["tox"]  

