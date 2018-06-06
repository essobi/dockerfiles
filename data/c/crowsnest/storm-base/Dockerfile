FROM alpine:3.4  
  
MAINTAINER Josh Sorenson <josh@crowsnest.io>  
  
RUN mkdir -p /opt  
  
RUN apk add --update tar curl gnupg python openjdk8 bash  
  
RUN gpg --recv-keys E80B8FFD  
RUN curl -s https://archive.apache.org/dist/storm/apache-storm-1.0.2/apache-
storm-1.0.2.tar.gz.asc -o apache-storm-1.0.2.tar.gz.asc && \  
curl -s https://archive.apache.org/dist/storm/apache-storm-1.0.2/apache-
storm-1.0.2.tar.gz -o apache-storm-1.0.2.tar.gz && \  
gpg --verify apache-storm-1.0.2.tar.gz.asc apache-storm-1.0.2.tar.gz && \  
tar zxf apache-storm-1.0.2.tar.gz -C /opt && \  
mv /opt/apache-storm-1.0.2 /opt/apache-storm && \  
rm apache-storm-1.0.2.tar.gz apache-storm-1.0.2.tar.gz.asc  
  
ADD configure.sh /  

