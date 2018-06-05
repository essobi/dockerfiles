FROM tifayuki/java:8  
MAINTAINER Kristofor Davison  
  
# add some OS tools  
RUN apt-get update && \  
apt-get install -y unzip wget curl && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
# set the timezone to London  
RUN echo Europe/London > /etc/timezone && \  
dpkg-reconfigure --frontend noninteractive tzdata  
  
# this will add AND UNPACK the kafka bundle...  
ADD kafka_2.11-0.10.0.0.tgz /opt  
ENV KAFKA_HOME /opt/kafka_2.11-0.10.0.0  
ADD startup.sh /startup.sh  
RUN chmod +x /startup.sh  
  
CMD ["/startup.sh"]  

