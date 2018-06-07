#  
# MongoDB Dockerfile  
#  
# https://github.com/dockerfile/mongodb  
#  
# Pull base image.  
FROM dockerfile/ubuntu  
  
# Install MongoDB.  
RUN \  
apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 7F0CEB10 && \  
echo "deb http://repo.mongodb.org/apt/ubuntu "$(lsb_release -sc)"/mongodb-
org/3.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-3.0.list &&
\  
apt-get update && \  
apt-get install -y mongodb-org=3.0.1&& \  
rm -rf /var/lib/apt/lists/*  
  
# Define mountable directories.  
VOLUME ["/data/db"]  
  
# Define working directory.  
WORKDIR /data  
  
# Define default command.  
CMD ["mongod"]  
  
# Expose ports.  
# - 27017: process  
# - 28017: http  
EXPOSE 27017  
EXPOSE 28017  

