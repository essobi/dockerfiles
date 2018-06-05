FROM openjdk:8  
  
RUN apt-get update && apt-get -y install python3 python3-pip && rm -rf
/var/lib/apt/lists && apt-get clean  
RUN pip3 install esrally  
RUN esrally configure  
  
ENV ES_HOSTNAME='elasticsearch.domain.name:9200'  
  
  
CMD esrally \--pipeline=benchmark-only \--target-hosts=${ES_HOSTNAME}
\--track=${RALLY_TRACK}  

