FROM nginx:alpine  
  
# Use https://github.com/just-containers/s6-overlay to get the s6 process
supervisor.  
ADD https://github.com/just-
containers/s6-overlay/releases/download/v1.11.0.1/s6-overlay-amd64.tar.gz
/tmp/  
RUN gunzip -c /tmp/s6-overlay-amd64.tar.gz | tar -xf - -C /  
ENTRYPOINT ["/init"]  
  
RUN echo "@edge-community http://dl-cdn.alpinelinux.org/alpine/edge/community"
>> /etc/apk/repositories  
RUN apk update \  
&& apk add --no-cache python py-pip groff lego@edge-community  
  
# These requirements for awscli caused the install to fail if attempted after
upgrading pip (and there are other requirements that caused the install to
fail if attempted before upgrading pip).  
RUN pip install 'rsa<=3.3.0,>=3.1.2' six  
RUN pip install --upgrade pip  
RUN pip install awscli  
  
COPY etc /etc  
RUN chmod -R +x /etc/periodic/  
  
CMD ["nginx", "-g", "daemon off;"]  
  

