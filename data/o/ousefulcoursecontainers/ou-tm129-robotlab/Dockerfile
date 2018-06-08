#Base container  
FROM dit4c/dit4c-container-x11:debian  
  
#Required in order to add backports repo  
RUN apt-get update && apt-get install -y software-properties-common  
  
RUN dpkg --add-architecture i386  
RUN echo "deb http://httpredir.debian.org/debian jessie-backports main" | sudo
tee /etc/apt/sources.list.d/docker.list  
RUN apt-get update && apt-get install -y -t jessie-backports wine  
  
# /var contains HTML site for container homepage  
COPY var /var  
  
# RobotLab windows files  
COPY Apps/ /opt/Apps  
  
# profile.d environment vars  
COPY etc /etc  
  
# Desktop shortcuts and application icons  
COPY usr /usr  
RUN chmod +x /usr/share/applications/robotlab.desktop  
RUN chmod +x /usr/share/applications/neural.desktop  
  
#Add items to top toolrail on desktop  
RUN LNUM=$(sed -n '/launcher_item_app/=' /etc/tint2/panel.tint2rc | head -1)
&& \  
sed -i "${LNUM}ilauncher_item_app = /usr/share/applications/robotlab.desktop"
/etc/tint2/panel.tint2rc && \  
sed -i "${LNUM}ilauncher_item_app = /usr/share/applications/neural.desktop"
/etc/tint2/panel.tint2rc  
  

