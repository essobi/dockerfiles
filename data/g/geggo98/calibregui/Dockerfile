# Dockerfile for a graphical Calibre service. It can be used to automatically  
# downoad external data, convert it in ebook format and add it to a Calibre  
# library and optinally send it per mail.  
#  
# Author: stefan@schwetschke.de  
# Date: 2015-01-18  
FROM geggo98/x11-vnc  
MAINTAINER Stefan Schwetschke "stefan@schwetschke.de"  
# Installing depdencies  
RUN apt-get update -y && \  
apt-get install -y curl wget xdg-utils python xz-utils && \  
apt-get clean  
  
# Installing calibre. This can take 5 minutes...  
ENV REFRESHED_CALIBRE_AT 2016-02-20  
RUN curl --silent --show-error
https://raw.githubusercontent.com/kovidgoyal/calibre/master/setup/linux-
installer.py \  
| sudo python -c "import sys; main=lambda:sys.stderr.write('Download
failed\n'); exec(sys.stdin.read()); main()" \  
2| grep -v -e '^Downloaded'  
  
ENV X11_USER calibre  
  
EXPOSE 8080  
VOLUME "/home/${X11_USER}/Calibre Library"  
VOLUME "/home/${X11_USER}/.config/calibre"  
  
# Start lxde with Calibe GUI.  
# When starting Calibre for the first time, you should  
# connect to the UI and finish the installation wizard  
CMD ["/opt/calibre/calibre"]  

