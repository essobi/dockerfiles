FROM debian  
MAINTAINER lagertonne mail@lagertonne.de  
  
RUN apt-get update -y && apt-get upgrade -y && \  
apt-get install -y wget lib32gcc1  
  
RUN cd /root && \  
mkdir content Steam content/css && cd Steam && \  
wget http://media.steampowered.com/installer/steamcmd_linux.tar.gz && \  
tar -xvzf steamcmd_linux.tar.gz  
  
RUN cd /root/Steam && ./steamcmd.sh +login anonymous +quit  
  
RUN mkdir /root/cs16 && cd /root/Steam && \  
./steamcmd.sh +login anonymous +force_install_dir "/root/cs16" +app_update 90
validate +quit && \  
./steamcmd.sh +login anonymous +force_install_dir "/root/cs16" +app_update 90
validate +quit && \  
rm -r /root/cs16/steamapps/*  
  
RUN cd /root/cs16/steamapps && wget
https://raw.githubusercontent.com/dgibbs64/HLDS-
appmanifest/master/appmanifest_70.acf && \  
~/Steam/steamcmd.sh +login anonymous +force_install_dir "/root/cs16"
+app_update 90 validate +quit; exit 0  
  
RUN cd /root/cs16/steamapps && wget
https://raw.githubusercontent.com/dgibbs64/HLDS-
appmanifest/master/appmanifest_10.acf && \  
~/Steam/steamcmd.sh +login anonymous +force_install_dir "/root/cs16"
+app_update 90 validate +quit; exit 0  
  
RUN cd /root/cs16/steamapps && \  
wget https://raw.githubusercontent.com/dgibbs64/HLDS-
appmanifest/master/appmanifest_90.acf && \  
~/Steam/steamcmd.sh +login anonymous +force_install_dir "/root/cs16"
+app_update 90 validate +quit  
  
# Install Metamod  
RUN mkdir -p /root/cs16/cstrike/addons/metamod/dlls  
  
RUN cd /root/cs16/cstrike/addons/metamod/dlls && \  
wget https://files.nscodes.com/cs16/metamod-p-1.21p37-linux_i686.tar.gz && \  
tar -xvzf metamod-p-1.21p37-linux_i686.tar.gz  
  
RUN touch /root/cs16/cstrike/addons/metamod/plugins.ini && \  
sed -i '/gamedll_linux/c\gamedll_linux \"addons\/metamod\/dlls\/metamod.so\"'
/root/cs16/cstrike/liblist.gam  
  
# Install amxmodx  
RUN cd /root/cs16/cstrike/ && \  
wget https://files.nscodes.com/cs16/amxmodx-1.8.2-base-linux.tar.gz && \  
tar xvfz amxmodx-1.8.2-base-linux.tar.gz  
  
RUN cd /root/cs16/cstrike/ && \  
wget https://files.nscodes.com/cs16/amxmodx-1.8.2-cstrike-linux.tar.gz && \  
tar xzvf amxmodx-1.8.2-cstrike-linux.tar.gz  
  
RUN cd /root/cs16/cstrike/addons/metamod && \  
echo "linux addons/amxmodx/dlls/amxmodx_mm_i386.so" >> plugins.ini  
  
EXPOSE 27016/udp  
  
WORKDIR /root/cs16  
  
ENTRYPOINT ["./hlds_run", "-game cstrike", "-insecure", "-port 27016",
"+maxplayers 32", "-console", "+map de_dust2", "+sv_lan 1"]  
  

