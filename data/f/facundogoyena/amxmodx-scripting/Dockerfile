FROM steeb/steamos-32  
  
# Configuration  
ENV DEBIAN_FRONTEND noninteractive  
  
# Dependencies  
USER root  
RUN apt-get update -qq && \  
apt-get install -y -qq --no-install-recommends \  
wget \  
unzip \  
ca-certificates  
  
# AMX Mod X  
WORKDIR /root/  
  
RUN wget -q -O amxx.tar.gz "http://www.amxmodx.org/release/amxmodx-1.8.2-base-
linux.tar.gz" && \  
tar --extract --gunzip --strip 3 --file amxx.tar.gz \  
addons/amxmodx/scripting/amxxpc \  
addons/amxmodx/scripting/amxxpc32.so \  
addons/amxmodx/scripting/include/  
  
RUN echo "\  
#!/bin/bash\n\  
cd /root/\n\  
./amxxpc \$1" > /usr/bin/amxxcompiler && \  
chmod +x /usr/bin/amxxcompiler  

