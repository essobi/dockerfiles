FROM java:7  
MAINTAINER kennethzfeng@gmail.com  
  
ENV ARCHIVA_DIR /opt/archiva  
  
RUN curl -sSLo /tmp/apache-archiva-2.1.1-bin.tar.gz
http://download.nextag.com/apache/archiva/2.1.1/binaries/apache-
archiva-2.1.1-bin.tar.gz \  
&& tar xzvf /tmp/apache-archiva-2.1.1-bin.tar.gz --directory /opt  
  
RUN mv /opt/apache-archiva-2.1.1 ARCHIVA_DIR  
  
RUN adduser archiva  
RUN chown -R archiva:archiva ARCHIVA_DIR  
  
WORKDIR ARCHIVA_DIR  
  
EXPOSE 8080  
USER archiva  
CMD bin/archiva console  

