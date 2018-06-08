FROM ubuntu:latest  
  
# Update OS  
RUN apt-get update  
RUN apt-get -y upgrade  
  
RUN apt-get install -y python-dev python-pip  
RUN apt-get install -y libffi-dev libssl-dev  
  
RUN pip install flanker  
RUN pip install elasticsearch  
  
  
# Add requirements.txt  
RUN mkdir /opt/mailgunflanker  
ADD 2es.py /opt/mailgunflanker/2es.py  
  
  
# Set the default directory for our environment  
ENV HOME /opt/mailgunflanker  
  
ENV EMAILS_PATH /var/mailgunflanker  
ENV ELASTICSEARCH "http://elasticserach:9200"  
ENV ELASTICSEARCH_INDEX "mailgunflanker"  
  
WORKDIR /opt/mailgunflanker  
  
CMD /usr/bin/python2.7 /opt/mailgunflanker/2es.py

