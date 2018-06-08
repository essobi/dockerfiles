FROM ubuntu:trusty  
  
# Install Git  
RUN apt-get update && apt-get install -y git vim  
  
# Install NodeJS  
RUN apt-get update --fix-missing && apt-get upgrade -y  
RUN apt-get install -y wget curl build-essential patch git-core openssl
libssl-dev unzip ca-certificates  
RUN curl http://nodejs.org/dist/v0.12.7/node-v0.12.7-linux-x64.tar.gz | tar
xzvf - --strip-components=1 -C "/usr"  
RUN apt-get clean && rm -rf /var/cache/apt/archives/* /var/lib/apt/lists/*  
  
# Clone Lineshell  
RUN git clone https://github.com/TehesFR/Lineshell /lineshell  
RUN cd /lineshell; npm install; npm install -g nodemon  
  
# Install MongoDB 3.0.7  
RUN DEBIAN_FRONTEND=noninteractive && \  
apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 7F0CEB10 && \  
echo "deb http://repo.mongodb.org/apt/ubuntu trusty/mongodb-org/3.0
multiverse" | tee /etc/apt/sources.list.d/mongodb-org-3.0.list && \  
apt-get update && \  
apt-get install -y --force-yes mongodb-org=3.0.7 mongodb-org-server=3.0.7
mongodb-org-shell=3.0.7 mongodb-org-mongos=3.0.7 mongodb-org-tools=3.0.7 && \  
service mongod stop && \  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Add scripts  
ADD scripts /scripts  
RUN chmod +x /scripts/*.sh  
RUN touch /.firstrun  
  
# Command to run  
ENTRYPOINT ["/scripts/run.sh"]  
CMD [""]  
  
# Expose listen port  
EXPOSE 8080  
# Set working directory  
WORKDIR /lineshell  
  
# Expose our data volumes  
VOLUME ["/data"]  

