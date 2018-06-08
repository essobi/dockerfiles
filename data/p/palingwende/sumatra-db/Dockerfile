FROM ubuntu:14.04  
# Update packages  
RUN apt-get update -y  
  
# Install and configure mongodb  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 7F0CEB10  
RUN echo "deb http://repo.mongodb.org/apt/ubuntu "$(lsb_release -sc)"/mongodb-
org/3.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-3.0.list  
RUN apt-get update -y  
RUN apt-get install -y mongodb-org  
RUN mkdir -p /data/db  
  
# Add and install Python modules here  
# Bundle app source  
ADD . /src  
  
# Expose  
EXPOSE 27017  
EXPOSE 28017  
# Adding a Volume for the db  
VOLUME ["/data"]  
  
# Run  
CMD ["usr/bin/mongod", "--rest"]

