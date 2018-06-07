FROM docker:stable-dind  
  
# https://github.com/docker/compose/issues/4967  
RUN apk update && \  
apk add bash make git openssh-client && \  
apk add --no-cache py-pip && \  
pip install docker==2.4.2 && \  
pip install docker-compose && \  
rm -rf /var/cache/apk/* /var/tmp/* /tmp/*  
  
COPY . /harpoon  
  
ENV PATH /harpoon:$PATH

