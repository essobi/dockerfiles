FROM aspirinsjl/nodejs  
  
# Note that REDIS_SERVER_VERSION is not used yet  
ENV REDIS_SERVER_VERSION=3.0.1 \  
MONGODB_VERSION=3.0.3  
# Learn from tutum, but conservatively keep apt list  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv C7917B12 && \  
apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y redis-server && \  
apt-get clean  
  
# Learn from mongodb official guide  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 7F0CEB10 && \  
echo "deb http://repo.mongodb.org/apt/ubuntu "$(lsb_release -sc)"/mongodb-
org/3.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-3.0.list &&
\  
apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y \  
mongodb-org=${MONGODB_VERSION} \  
mongodb-org-server=${MONGODB_VERSION} \  
mongodb-org-shell=${MONGODB_VERSION} \  
mongodb-org-mongos=${MONGODB_VERSION} \  
mongodb-org-tools=${MONGODB_VERSION} && \  
echo "mongodb-org hold" | sudo dpkg --set-selections && \  
echo "mongodb-org-server hold" | sudo dpkg --set-selections && \  
echo "mongodb-org-shell hold" | sudo dpkg --set-selections && \  
echo "mongodb-org-mongos hold" | sudo dpkg --set-selections && \  
echo "mongodb-org-tools hold" | sudo dpkg --set-selections  

