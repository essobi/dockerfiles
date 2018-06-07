# This is a docker Drupal environment for PNX QA and Staging.  
#  
FROM previousnext/base:latest  
MAINTAINER Nick Schuch <nick@previousnext.com.au>  
  
##  
# Packages.  
##  
RUN apt-add-repository 'deb http://au.archive.ubuntu.com/ubuntu precise main'  
RUN apt-add-repository 'deb http://au.archive.ubuntu.com/ubuntu precise-
updates main'  
RUN apt-get update -y  
RUN apt-get install -y openjdk-7-jre-headless tar  
  
##  
# Configure DynamoDB.  
##  
RUN mkdir -p /opt/dynamodb  
RUN mkdir -p /opt/dynamodb/data  
ADD http://dynamodb-local.s3-website-us-
west-2.amazonaws.com/dynamodb_local_latest.tar.gz /opt/dynamodb.tar.gz  
RUN tar -C /opt/dynamodb --extract --file /opt/dynamodb.tar.gz  
  
##  
# Startup scripts.  
##  
ADD ./scripts/start.sh /root/start.sh  
RUN chmod 755 /root/start.sh  
  
##  
# Setup supervisord.  
##  
ADD ./conf/supervisor/supervisord.conf /etc/supervisord.conf  
  
EXPOSE 8000  
CMD ["/root/start.sh"]  

