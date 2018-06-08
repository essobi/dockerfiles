#  
# nodervisor Dockerfile  
#  
# to build:  
# `docker build -t nodervisor .`  
# to run, using sqlite database bind-mounted from host system:  
# `touch nodervisor.sqlite`  
# `docker run -p 3000:3000 -v
nodervisor.sqlite:/opt/nodervisor/nodervisor.sqlite nodervisor`  
FROM ubuntu:14.04  
MAINTAINER "Joshua C. Randall" <jcrandall@alum.mit.edu>  
  
# Install prerequisites  
RUN \  
apt-get -q=2 update && \  
apt-get -q=2 upgrade && \  
apt-get -q=2 install coreutils npm nodejs && \  
ln -s /usr/bin/nodejs /usr/bin/node && \  
npm install express --global  
  
# Install nodervisor from git  
ADD . /opt/nodervisor  
WORKDIR /opt/nodervisor  
  
# Install npm packages for nodervisor  
RUN npm install  
  
# Run npm start by default  
CMD ["/usr/bin/npm","start"]  

