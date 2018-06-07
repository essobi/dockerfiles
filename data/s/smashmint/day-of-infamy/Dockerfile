FROM gameye/steamcmd  
USER root  
  
RUN dpkg --add-architecture i386  
RUN apt-get update -q && \  
apt-get install \  
libstdc++6:i386 \  
libcurl4-gnutls-dev:i386 \  
lib32z1 \  
lib32ncurses5 \  
libbz2-1.0:i386 \  
lib32gcc1 \  
gdb -y && \  
apt-get clean  
  
USER steam  
RUN ./steamcmd.sh \  
+login anonymous \  
+force_install_dir /home/steam/doi \  
+app_update 462310 validate \  
+quit  
  
WORKDIR /home/steam/doi  
ENTRYPOINT ["/home/steam/doi/srcds_run"]  

