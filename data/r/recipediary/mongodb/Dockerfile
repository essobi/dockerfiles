# Install a more up to date mongodb than what is included in the default
ubuntu repositories.  
#  
# https://github.com/kstaken/dockerfile-
examples/blob/master/mongodb/Dockerfile  
# http://docs.docker.io/en/latest/examples/mongodb/  
# http://docs.mongodb.org/manual/tutorial/install-mongodb-on-ubuntu/  
# trusty (14.04) minimal  
FROM ubuntu:14.04.1  
# Add 10gen official apt source to the sources list  
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv 7F0CEB10  
RUN echo 'deb http://downloads-distro.mongodb.org/repo/ubuntu-upstart dist
10gen' | tee -a /etc/apt/sources.list.d/mongodb.list  
  
# Install MongoDB  
ENV MONGODB_VERSION 2.6.5  
RUN apt-get update && \  
apt-get -yq install mongodb-org=${MONGODB_VERSION} && \  
mkdir -p /data/db && \  
rm -rf /var/lib/apt/lists/*  
  
# run as the daemon user  
# USER daemon  
# define mountable directories  
VOLUME ["/data/db"]  
  
# define working directory.  
WORKDIR /data  
  
# expose ports  
# - 27017: process  
# - 28017: http  
EXPOSE 27017  
EXPOSE 28017  
# ENTRYPOINT ["usr/bin/mongod", "--dbpath", "data/db"]  
# define default command  
#CMD ["--smallfiles"]  
CMD ["mongod"]  

