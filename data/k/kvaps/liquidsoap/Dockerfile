FROM debian:wheezy  
MAINTAINER kvaps <kvapss@gmail.com>  
  
# Install Liquidsoap  
RUN apt-get -q update && \  
apt-get -q -y install liquidsoap liquidsoap-plugin-all sudo curl  
  
# Install aacplus encoder  
RUN echo "deb http://www.deb-multimedia.org wheezy main non-free" >>
/etc/apt/sources.list && \  
curl -O http://www.deb-multimedia.org/pool/main/d/deb-multimedia-keyring/deb-
multimedia-keyring_2015.6.1_all.deb && \  
sudo dpkg -i deb-multimedia-keyring_2015.6.1_all.deb  
RUN apt-get -q update && apt-get -q -y install aacplusenc  
  
# Telnet control  
EXPOSE 1337  
# live harbour  
EXPOSE 8000  
VOLUME ["/config"]  
  
ENTRYPOINT ["/usr/bin/sudo", "-u", "liquidsoap", "liquidsoap",
"/config/radio.liq"]  
  
WORKDIR /root  
  

