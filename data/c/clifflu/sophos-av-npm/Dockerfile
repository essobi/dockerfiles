FROM maxpowa/sophos-av  
  
RUN wget -qO- https://deb.nodesource.com/setup_6.x | bash && apt-get install
-y nodejs && apt-get clean -y  
  
ONBUILD RUN apt-get update && apt-get upgrade -y && apt-get autoremove -y &&
apt-get clean -y  
ONBUILD RUN /opt/sophos-av/bin/savupdate -v5  
  
ENTRYPOINT []  

