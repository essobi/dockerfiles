FROM ubuntu:17.04  
RUN useradd --user-group --create-home --shell /bin/bash openra  
ENV HOME=/home/openra  
  
RUN cd /tmp && \  
apt-get update && \  
apt-get install -y wget mono-runtime libmono-cil-dev libsdl2-2.0 \  
libmono-system-core4.0-cil libmono-system-drawing4.0-cil libmono-system-
data4.0-cil \  
libmono-system-numerics4.0-cil libmono-system-runtime-serialization4.0-cil \  
libmono-system-xml-linq4.0-cil libgl1-mesa-dri liblua5.1-0 libopenal1
libgl1-mesa-glx xdg-utils \  
zenity && \  
wget
https://github.com/OpenRA/OpenRA/releases/download/release-20170527/openra_release.20170527_all.deb
-O openra.deb && \  
dpkg -i openra.deb && \  
rm openra.deb  
  
COPY launch-dedicated.sh $HOME/  
RUN chmod +x $HOME/launch-dedicated.sh && chown -R openra:openra $HOME/  
USER openra  
WORKDIR $HOME  
ENTRYPOINT ["/bin/bash", "-c", "$HOME/launch-dedicated.sh"]  

