FROM debian  
MAINTAINER kitsunedo13@gmail.com  
  
# Minecraft Server Version and Docker Container Image Build Number  
LABEL version="1.8.8-3"  
  
RUN apt-get update \  
&& apt-get install -y sudo curl openjdk-7-jre-headless  
  
# copy entrypoint script and create restricted user  
ADD assets /usr/local/sbin/  
RUN chmod +x /usr/local/sbin/entrypoint.sh  
  
RUN useradd -m -s /bin/bash minecraft  
  
RUN rm -rf /var/lib/apt/lists/*  
  
# Minecraft Server's default port number  
EXPOSE 25565  
ENTRYPOINT ["/usr/local/sbin/entrypoint.sh"]  
  

