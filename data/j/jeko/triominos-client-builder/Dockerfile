FROM jeko/phusion-ssh  
VOLUME /artifacts  
RUN DEBIAN_FRONTEND=noninteractive apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y docker.io && \  
rm -rf /var/lib/apt/lists/*  
VOLUME /var/lib/docker  
ENV ID_RSA= \  
ID_RSA_PUB=  
COPY ssh-config /root/.ssh/config  
COPY build.sh /build.sh  
CMD /build.sh  

