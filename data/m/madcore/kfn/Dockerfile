FROM ubuntu:16.04  
ENV PATH_BASE /var/kfn  
ENV PATH_DATA /opt/kfn  
  
RUN mkdir -p $PATH_BASE  
RUN mkdir -p $PATH_DATA  
  
ADD requirements.txt $PATH_BASE/requirements.txt  
ADD examples/consumer.py $PATH_BASE/examples/consumer.py  
ADD examples/producer.py $PATH_BASE/examples/producer.py  
ADD examples/neo.py $PATH_BASE/examples/neo.py  
  
RUN apt-get update  
RUN apt-get install librdkafka-dev libyajl-dev kafkacat python-pip dnsutils
nano -y  
  
RUN pip install -r $PATH_BASE/requirements.txt  
  

