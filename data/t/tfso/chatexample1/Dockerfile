# Dockerfile  
FROM tfso/server_nodejs_dockerfile:master  
RUN apt-get update \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
COPY . src/  
RUN cd /src/ && npm install

