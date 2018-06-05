FROM ubuntu:xenial  
  
RUN apt-get update -q && \  
apt-get upgrade -qy && \  
apt-get install -qy bzip2 && \  
apt-get install -qy libcurl4-openssl-dev && \  
apt-get install -qy mono-devel && \  
apt-get install -qy wget && \  
apt-get clean  
  
ADD launch.sh /launch.sh  
RUN chmod +x "/launch.sh"  
  
# http://www.htpcguides.com/install-jackett-ubuntu-15-x-for-custom-torrents-
in-sonarr/  
RUN cd /tmp && jackettver=$(wget -q
https://github.com/Jackett/Jackett/releases/latest -O - | grep -E \/tag\/ |
awk -F "[><]" '{print $3}') && \  
wget -q
https://github.com/Jackett/Jackett/releases/download/$jackettver/Jackett.Binaries.Mono.tar.gz  
RUN cd /tmp && tar -xvf Jackett*  
# ADD ["jackett.service", "/etc/systemd/system/jackett.service"]  
RUN adduser jackett  
#RUN addgroup jackett  
RUN adduser jackett jackett  
RUN mkdir /opt/jackett && mv /tmp/Jackett*/* /opt/jackett  
  
# RUN touch /etc/systemd/system/jackett.service  
RUN chown -R jackett:jackett /opt/jackett  
  
# RUN systemctl enable jackett && service jackett start  
EXPOSE 9117  
# CMD ["mono --debug /opt/NzbDrone/NzbDrone.exe"]  
CMD ["/launch.sh"]  

