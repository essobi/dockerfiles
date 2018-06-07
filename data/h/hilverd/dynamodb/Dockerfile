FROM openjdk:8  
MAINTAINER Hilverd Reker <me@hilverd.com>  
  
RUN mkdir /opt/dynamodb  
  
WORKDIR /opt/dynamodb  
  
RUN wget http://dynamodb-local.s3-website-us-
west-2.amazonaws.com/dynamodb_local_latest.tar.gz && \  
tar -zxf dynamodb_local_latest.tar.gz && \  
rm dynamodb_local_latest.tar.gz  
  
COPY ./entrypoint /usr/local/bin/entrypoint  
  
VOLUME /databases  
  
EXPOSE 8000  
ENTRYPOINT ["entrypoint"]  
  
CMD ["-sharedDb"]  

