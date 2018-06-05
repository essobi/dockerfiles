FROM alpine:3.6  
ADD http://git.io/weave /usr/local/bin/weave  
  
RUN apk update && \  
apk add curl && \  
apk add bind-tools && \  
apk add fish && \  
apk add docker && \  
apk add nmap && \  
apk add --no-cache python3 && \  
pip3 install --upgrade pip setuptools httpie && \  
chmod a+x /usr/local/bin/weave  
  
CMD ["tail", "-f", "/dev/null"]

