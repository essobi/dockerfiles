FROM ibmcom/ibmnode:latest  
MAINTAINER Riccardo B. Desantis <riccardobenito.desantis@gmail.com>  
  
# Setting the environment  
ENV HOSTNAME rrdtool.rickdesantis.docker.com  
ENV USERHOME /root  
ENV DEBIAN_FRONTEND noninteractive  
ENV USER root  
ENV NAME docker  
ENV PASSWORD docker  
ENV PORT 13910  
ENV S_PORT 13911  
ENV RRD_PATH /opt/rrdtool  
ENV DATA_PATH /opt/rrd-data  
  
# Update the repos and install all the used packages  
RUN apt-get update && \  
(apt-get install -y --no-install-recommends curl build-essential
libglib2.0-dev libxml2-dev libpango1.0-dev groff; \  
while [ $? -ne 0 ]; do apt-get install -y --no-install-recommends curl build-
essential libglib2.0-dev libxml2-dev libpango1.0-dev groff; done) && \  
apt-get autoclean && \  
apt-get autoremove && \  
rm -rf /var/lib/apt/lists/*  
  
# Fixes Node.JS on Docker  
RUN cd $(npm root -g)/npm && \  
npm install fs-extra && \  
sed -i -e s/graceful-fs/fs-extra/ -e s/fs.rename/fs.move/
./lib/utils/rename.js  
  
# Download and install RDDTool  
WORKDIR $USERHOME  
RUN curl http://oss.oetiker.ch/rrdtool/pub/rrdtool-1.6.0.tar.gz -OL && \  
tar zxf rrdtool-1.6.0.tar.gz && \  
mkdir -p $RRD_PATH && \  
cd rrdtool-1.6.0 && ./configure --prefix=$RRD_PATH && make && make install  
  
# Copy the Node.JS application and install the dependencies  
COPY node $USERHOME/node  
WORKDIR $USERHOME/node  
RUN npm install  
  
# Starts the Node.JS server  
EXPOSE $PORT  
EXPOSE $S_PORT  
CMD $RRD_PATH/bin/rrdcached -L -F && npm run-script pm2-start  
  
# Build: docker build -t database-ts ../database-ts  
# Run: docker run --name=database-ts -p 13910:13910 -p 13911:13911 database-ts
&  
# Bash: docker exec -it database-ts bash  
# Start: docker start database-ts  
# Stop: docker stop database-ts  

