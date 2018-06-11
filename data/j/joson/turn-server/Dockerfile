# original inited,clone from zolochevska/turn-server,then modi by joson  
FROM ubuntu:16.04  
MAINTAINER joson chen <josonchen@sina.com>  
ENV REFRESHED_AT 20180320  
# Set the working directory to /app  
WORKDIR /app  
  
# Copy the current directory contents into the container at /app  
ADD . /app  
  
EXPOSE 3478  
RUN apt-get -yqq update && apt-get install -y \  
dnsutils \  
coturn \  
&& rm -rf /var/lib/apt/lists/*  
  
ENTRYPOINT ["bash", "deploy-turnserver.sh"]  

