FROM golang:1.5  
MAINTAINER Chris Gibson <git@twoitguys.com>  
  
# Clone letsencrypt.sh repo  
RUN cd /srv && git clone \--depth 1
https://github.com/lukas2511/letsencrypt.sh.git letsencrypt  
RUN chmod +x /srv/letsencrypt/letsencrypt.sh  
  
# Install doctl  
RUN go get github.com/digitalocean/doctl/cmd/doctl  
  
# Copy hooks  
ADD container-files /  
RUN chmod +x /srv/letsencrypt/letsencrypt.default.sh  
RUN chmod +x /run.sh  
  
# Entrypoint  
ENTRYPOINT ["/run.sh"]  
  

