# Version 0.0.5  
FROM fedora:latest  
MAINTAINER Roy P "meltingrobot@gmail.com"  
RUN dnf -y update  
RUN dnf -y install mediainfo libzen libmediainfo gettext mono-core mono-devel
sqlite.x86_64 wget telnet  
RUN wget http://download.sonarr.tv/v2/master/mono/NzbDrone.master.tar.gz  
RUN tar -xvf NzbDrone.master.tar.gz -C /opt/  
CMD [ "/bin/bash", "-c", "/usr/bin/mono /opt/NzbDrone/NzbDrone.exe -nobrowser
-data /opt/NzbDrone" ]  
VOLUME /opt/NzbDrone  
EXPOSE 8989  

