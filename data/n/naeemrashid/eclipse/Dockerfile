FROM ubuntu:14.04  
RUN apt-get update && apt-get install -y software-properties-common \  
hicolor-icon-theme \  
libgl1-mesa-dri \  
libgl1-mesa-glx \  
libpango1.0-0 \  
ca-certificates \  
openjdk-7-jdk \  
eclipse --no-install-recommends \  
&& rm -rf /var/lib/apt/lists/* \  
&& mkdir -p /root/.eclipse/  
#RUN useradd --create-home --home-dir $HOME eclipse \  
# && chown -R eclipse:eclipse $HOME \  
# && mkdir $HOME/workspace  
ENTRYPOINT [ "eclipse" ]  

