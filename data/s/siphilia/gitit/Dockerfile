FROM ubuntu:16.04  
ADD files/ /  
  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get update && \  
apt-get install --no-install-recommends -y gitit supervisor && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* && \  
groupadd gitit && \  
useradd -d /data -g gitit gitit && \  
chown -R gitit:gitit /data && \  
chmod 700 docker-entrypoint.sh  
  
EXPOSE 5001  
CMD ["/docker-entrypoint.sh"]  

