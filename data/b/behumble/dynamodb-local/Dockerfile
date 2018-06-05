FROM openjdk:8-jre  
MAINTAINER Alan Goo <behumble@hanjava.net>  
  
# will be executed while building the image.  
RUN /usr/bin/curl -L https://s3-us-west-2.amazonaws.com/dynamodb-
local/dynamodb_local_latest.tar.gz | /bin/tar xz  
COPY app-entrypoint.sh /  
RUN chmod a+x app-entrypoint.sh  
  
# will be executed when starting a container.  
ENTRYPOINT ["./app-entrypoint.sh"]  
  
# default arguments  
CMD []  
  
# DynamoDB Local is listening on port 8000 by default  
EXPOSE 8000  

