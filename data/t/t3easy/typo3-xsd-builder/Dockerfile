FROM composer:1.3  
ADD app /app/  
  
ADD bootstrap.sh /bootstrap.sh  
ADD generatexsd.sh /generatexsd.sh  
ADD teardown.sh /teardown.sh  
  
RUN mkdir /xsd  
  
RUN /bootstrap.sh \  
&& /generatexsd.sh 7.6 8.5 8.6 master \  
&& /teardown.sh  
  
VOLUME /xsd  
  
CMD ["ls", "-l", "/xsd"]

