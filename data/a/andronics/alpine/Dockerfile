FROM alpine:edge  
  
LABEL author="andronics <andronics@gmail.com>"  
  
ADD https://github.com/just-
containers/s6-overlay/releases/download/v1.21.2.2/s6-overlay-amd64.tar.gz
/tmp/  
ADD https://github.com/jwilder/docker-gen/releases/download/0.7.4/docker-gen-
linux-amd64-0.7.4.tar.gz /tmp/  
  
RUN tar xzf /tmp/s6-overlay-amd64.tar.gz -C / && \  
rm /tmp/s6-overlay-amd64.tar.gz && \  
tar xzf /tmp/docker-gen-linux-amd64-0.7.4.tar.gz -C /bin && \  
rm /tmp/docker-gen-linux-amd64-0.7.4.tar.gz && \  
chmod 0755 /bin/docker-gen  
  
ENTRYPOINT /init

