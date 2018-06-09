FROM golang:1.9.4-stretch  
  
LABEL Description="A docker container of Go language + dep, to be used to
reduce the build time of your final image."  
  
RUN curl -fsSL -o /usr/local/bin/dep
https://github.com/golang/dep/releases/download/v0.4.1/dep-linux-amd64 && \  
chmod +x /usr/local/bin/dep  

