############################################################  
# Dockerfile to run and restore mongo dump files  
# Based on mongo 3.2 Image  
############################################################  
  
FROM mongo:3.2  
MAINTAINER Atif Saddique <atif@aurorasolutions.io>  
  
  
#---------- Configure Users  
  
# configure the "navigator" and "root" users  
RUN echo 'root:navigator' |chpasswd  
RUN groupadd navigator && useradd navigator -s /bin/bash -m -g navigator -G
navigator && adduser navigator sudo  
RUN echo 'navigator:navigator' |chpasswd  
RUN cd /home && chown -R navigator:navigator /home/navigator  
  
# Update aptitude with new repo  
RUN apt-get update  
  
# Install software  
RUN apt-get install -y git  
  
RUN apt-get install -y zip unzip vim  
  
VOLUME ["/home/navigator"]  
  
VOLUME ["/data/db"]  
  
# expose the mongo server port  
EXPOSE 27017  
  
ENTRYPOINT ["/usr/bin/mongod"]  
  
CMD ["--port", "27017", "--dbpath", "/data/db", "--smallfiles"]  

