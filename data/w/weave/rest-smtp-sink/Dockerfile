FROM progrium/busybox  
MAINTAINER Garth Johnson <dockerfiles@ambled.org>  
  
# clone busybox+node solution from hwestphal/docker-nodebox  
RUN opkg-install curl bash git libstdcpp && \  
rm -f /lib/libpthread.so.0 && \  
ln -s /lib/libpthread-2.18.so /lib/libpthread.so.0 && \  
curl -s http://nodejs.org/dist/v0.10.36/node-v0.10.36-linux-x64.tar.gz |
gunzip | tar -xf - -C /  
  
ENV PATH /node-v0.10.36-linux-x64/bin:$PATH  
  
# Don't break Docker cache if package.json has not changed  
ADD package.json /tmp/package.json  
RUN cd /tmp && \  
npm install && \  
mkdir -p /opt/rest-smtp-sink && \  
mv /tmp/node_modules /opt/rest-smtp-sink && \  
rm -rf /tmp/*  
  
# Add the rest of the code from this repo  
WORKDIR /opt/rest-smtp-sink  
ADD LICENSE cli.js index.js package.json test /opt/rest-smtp-sink/  
  
# Use standard ports by default for use with linked containers  
EXPOSE 25 80  
CMD ["node", "cli", "--listen", "80", "--smtp", "25"]  
  

