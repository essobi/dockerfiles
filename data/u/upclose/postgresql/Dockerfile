FROM gliderlabs/alpine:3.2  
RUN apk -U add openssl && \  
wget -qO- https://github.com/Rushmorefm/alpine-
packages/releases/download/v0.1/testing.tar.xz | tar xJ && \  
apk --allow-untrusted -X /testing -X
http://dl-2.alpinelinux.org/alpine/edge/testing -U add postgresql postgresql-
contrib postgis && \  
rm -rf /testing /var/cache/apk/*  
  
# required to ensure that we can insert a userid intodb  
RUN chmod a+w /etc/passwd  
  
CMD ["/host/postgresql/scripts/start"]  

