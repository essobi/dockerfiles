FROM mono  
  
LABEL maintainer="willietgwb@gmail.com"  
  
RUN apt-get update && apt-get install -y \  
wget \  
unzip  
  
#COPY start.sh /start  
ENV ECO_VERSION=0.7.4.6  
RUN mkdir /eco && \  
cd /eco && \  
wget https://s3-us-west-2.amazonaws.com/eco-releases/EcoServer_v$ECO_VERSION-
beta.zip && \  
unzip EcoServer_v$ECO_VERSION-beta.zip && \  
rm EcoServer_v$ECO_VERSION-beta.zip && \  
chmod +x /eco/EcoServer.exe  
#chmod +x /start  
RUN apt-get purge -y \  
wget \  
unzip && \  
apt-get autoremove -y && \  
rm -rf /var/lib/apt/lists/* && \  
rm -rf /eco/Configs && \  
rm -rf /eco/Storage && \  
rm -rf /eco/Mods && \  
rm -rf /eco/Logs  
  
# Back to the working directory for the server  
WORKDIR /eco  
  
EXPOSE 2999/udp 3000 3001  
VOLUME [/eco/Configs, /eco/Storage, /eco/Mods, /eco/Logs]  
  
#ENTRYPOINT ["/start"]  
CMD ["mono", "--server", "--gc=sgen", "-O=all", "EcoServer.exe", "-nogui"]  

