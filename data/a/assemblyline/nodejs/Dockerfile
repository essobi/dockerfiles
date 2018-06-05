FROM assemblyline/buildpack_deps  
  
ENV NODE_VERSION 0.10.36  
COPY SHASUMS256.txt /SHASUMS256.txt  
  
RUN curl -SLO "http://nodejs.org/dist/v0.10.36/node-v0.10.36-linux-x64.tar.gz"
\  
&& cat SHASUMS256.txt | sha256sum -c - \  
&& tar -xzf "node-v0.10.36-linux-x64.tar.gz" -C /usr/local \--strip-
components=1 \  
&& rm "node-v0.10.36-linux-x64.tar.gz" SHASUMS256.txt  

