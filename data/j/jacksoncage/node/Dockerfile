# Node.js container  
#  
# docker run -rm -i -d \  
# -p 8080 \  
# -e EXECUTER=nodemon \  
# -e APP=app.js \  
# -v `pwd`/www:/var/www:ro \  
# -v /etc/localtime:/etc/localtime \  
# jacksoncage/node  
FROM debian:jessie  
MAINTAINER Love Nyberg "love.nyberg@lovemusic.se"  
ENV REFRESHED_AT 2015-12-11  
# Update the package repository  
RUN DEBIAN_FRONTEND=noninteractive apt-get update; apt-get upgrade -y  
  
# Compiling and installing node.js  
RUN DEBIAN_FRONTEND=noninteractive apt-get update -qq && \  
DEBIAN_FRONTEND=noninteractive apt-get upgrade -yqq && \  
DEBIAN_FRONTEND=noninteractive apt-get install -yqq wget curl python g++ make
checkinstall fakeroot && \  
src=$(mktemp -d) && cd $src && \  
wget -N http://nodejs.org/dist/node-latest.tar.gz && \  
tar xzvf node-latest.tar.gz && cd node-v* && \  
./configure && \  
fakeroot checkinstall -y --install=no --pkgversion $(echo $(pwd) | sed -n
-re's/.+node-v(.+)$/\1/p') make -j$(($(nproc)+1)) install && \  
dpkg -i node_* && \  
npm install -g nodemon forever  
  
# Clean image  
RUN apt-get -yqq clean && \  
apt-get -yqq purge && \  
rm -rf /tmp/* /var/tmp/* && \  
rm -rf /var/lib/apt/lists/*  
  
VOLUME /var/www  
WORKDIR /var/www  
EXPOSE 8080  
COPY start.sh /start.sh  
CMD ["bash", "start.sh"]  

