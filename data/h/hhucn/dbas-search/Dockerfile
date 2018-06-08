FROM docker.elastic.co/elasticsearch/elasticsearch:6.0.0  
MAINTAINER Christian Meter <meter@cs.uni-duesseldorf.de>  
  
RUN yum -y update && \  
yum -y install https://rhel7.iuscommunity.org/ius-release.rpm  
  
RUN yum -y install python36u python36u-pip  
  
ENV PYTHONPATH /code  
  
COPY . /code  
COPY search_service/config/elasticsearch.yml /usr/share/elasticsearch/config/  
COPY search_service/analysis/synonyms_english.txt
/usr/share/elasticsearch/config/synonyms_english.txt  
COPY search_service/analysis/synonyms_german.txt
/usr/share/elasticsearch/config/synonyms_german.txt  
  
USER root  
RUN chown elasticsearch:elasticsearch config/elasticsearch.yml && \  
chown -R elasticsearch:elasticsearch /code && \  
chown elasticsearch:elasticsearch
/usr/share/elasticsearch/config/synonyms_english.txt && \  
chown elasticsearch:elasticsearch
/usr/share/elasticsearch/config/synonyms_german.txt  
  
RUN pip3.6 install -r /code/search_service/requirements.txt && \  
touch /code/__init__.py  
  
USER elasticsearch  
  
EXPOSE 5000 9200  
CMD ["/code/docker_init.sh"]  

