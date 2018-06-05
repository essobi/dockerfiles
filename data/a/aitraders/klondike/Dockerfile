FROM mono:4.6.1.3  
ENV KLONDIKE_VERSION=v2.1.1  
ENV KLONDIKE_BUILD=2.1.1.22ea5477-build156  
  
RUN apt-get update && \  
apt-get install wget unzip mono-4.0-service && \  
rm -rf /var/cache/apt/*  
  
RUN mkdir /app && cd /app && wget
https://github.com/themotleyfool/Klondike/releases/download/${KLONDIKE_VERSION}/Klondike.${KLONDIKE_BUILD}.zip
-O /app/Klondike.${KLONDIKE_BUILD}.zip && \  
unzip *.zip  
  
EXPOSE 8080  
COPY Settings.config /app/Settings.config  
COPY variables.sh /etc/docker-image-variables.sh  
  
WORKDIR /app/bin  
CMD ["mono", "/usr/lib/mono/4.5/mono-service.exe", "./Klondike.SelfHost.exe",
"--port=8080"]  

