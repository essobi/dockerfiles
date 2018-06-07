FROM ubuntu:15.10  
RUN apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y lxde tightvncserver nano vim
curl && \  
rm -rf /var/lib/apt/lists/*  
  
COPY home/ /data/home  
COPY setup-start /usr/bin  
  
# Define default command.  
CMD ["setup-start"]  
  
# Expose ports.  
EXPOSE 5901

