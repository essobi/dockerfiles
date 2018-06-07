FROM alpine:latest  
  
LABEL maintainer "lavender.flowerdew@gmail.com"  
  
RUN apk update && apk upgrade && \  
apk --no-cache add \  
bash \  
ca-certificates \  
curl \  
openssl \  
sudo && \  
update-ca-certificates  
  
# Users  
RUN echo 'root:root' | chpasswd  
RUN addgroup -S flower && adduser -G flower -g "Lavender Flowerdew" -s
/bin/bash -D flower  
RUN echo 'flower:flower' | chpasswd  
RUN echo 'flower ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers  
  
# Clean Up  
RUN rm -rf /var/cache/apk/*  
  
# Set Up Environment  
# WORKDIR /home/flower  
# USER flower  
# Start container  
CMD ["/bin/sh", "-i"]  

