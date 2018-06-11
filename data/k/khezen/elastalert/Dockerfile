FROM debian:jessie  
  
MAINTAINER Guillaume Simonneau <simonneaug@gmail.com>  
LABEL Description="elasticsearch elastalert"  
  
ENV ELASTIC_PWD="changeme" \  
ELASTICSEARCH_HOST="elasticsearch" \  
ELASTICSEARCH_PORT="9200"  
RUN apt-get update -y && apt-get install curl -y  
ADD ./src/ /run/  
RUN chmod +x -R /run/  
  
RUN mkdir /.backup  
  
RUN /run/setup/elastalert.sh  
  
ENTRYPOINT ["/run/entrypoint.sh"]  
CMD ["python","/elastalert/elastalert/elastalert.py", "--config
/etc/elastalert/elastalert.yml", "--verbose"]  

