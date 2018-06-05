FROM progrium/busybox  
  
ADD http://nodejs.org/dist/v0.10.34/node-v0.10.34-linux-x64.tar.gz
/tmp/nodejs.tar.gz  
  
RUN \  
mkdir -p /usr/local/lib \  
&& gunzip /tmp/nodejs.tar.gz \  
&& tar xf /tmp/nodejs.tar -C /tmp \  
&& rm -rf /tmp/nodejs.tar \  
&& mv /tmp/node-* /usr/local/lib/nodejs  
  
ENV PATH $PATH:/usr/local/lib/nodejs/bin  

