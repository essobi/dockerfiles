FROM ubuntu:16.04  
RUN apt-get update -qq && \  
apt-get install --no-install-recommends --no-install-suggests -qqy ca-
certificates curl lib32gcc1 && \  
rm -rf /var/lib/apt/lists/* && \  
mkdir -p /opt/steamcmd && \  
cd /opt/steamcmd && \  
curl -s http://media.steampowered.com/installer/steamcmd_linux.tar.gz | tar
-xz && \  
./steamcmd.sh +login anonymous +force_install_dir /server +app_update "406800
validate" +exit && \  
rm -rf /opt/steamcmd && \  
useradd -b /server oor && \  
chown -R oor /server  
  
USER oor  
WORKDIR /server  
  
ENTRYPOINT ["SFS2X/sfs2x-service", "start-launchd"]  

