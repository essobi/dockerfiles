FROM ubuntu  
MAINTAINER ZhiFeng Hu <hufeng1987@gmail.com>  
RUN apt-get update && \  
apt-get install -y libappindicator3-1 wget && \  
wget https://raw.githubusercontent.com/getlantern/lantern-
binaries/master/lantern-installer-beta-64-bit.deb -O lantern-installer-
beta-64-bit.deb && \  
dpkg -i lantern-installer-beta-64-bit.deb  
EXPOSE 8787  
ENTRYPOINT [ "/usr/bin/lantern", "-headless", "-addr", "0.0.0.0:8787" ]  
#ENTRYPOINT [ "/usr/bin/lantern", "--help" ]  

