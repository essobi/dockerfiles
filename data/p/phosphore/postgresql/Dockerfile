FROM postgres:10.3  
  
RUN apt-get update && apt-get -yq install sudo daemontools pv python3-pip lzop
&& python3 -m pip install wal-e[swift] \  
&& apt-get autoclean  
  
ADD pgbkp.sh /sudokeys/  
  
RUN ln -fs /usr/share/zoneinfo/Europe/Paris /etc/localtime && dpkg-reconfigure
-f noninteractive tzdata  
RUN localedef -i fr_FR -c -f UTF-8 -A /usr/share/locale/locale.alias
fr_FR.UTF-8  

