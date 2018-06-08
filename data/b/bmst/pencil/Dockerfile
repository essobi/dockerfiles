FROM ubuntu:14.04  
MAINTAINER Bogdan Mustiata <bogdan.mustiata@gmail.com>  
  
#  
# This is just a default install of the pencil, with the following addons
already available  
# for installation (in the /extra/ folder):  
# * Pencil Material Template: https://github.com/DaniGuardiola/pencil-
material-template/  
# * Material Icons for Pencil: https://github.com/nathanielw/Material-Icons-
for-Pencil/  
# * Android Lollipop Pencil Stencils: https://github.com/nathanielw/Android-
Lollipop-Pencil-Stencils/  
# * Bootstrap Pencil Stencils: https://github.com/nathanielw/Bootstrap-Pencil-
Stencils/  
  
RUN apt-get update -y && apt-get upgrade -y && \  
apt-get install -y libgtk-3-0 libasound2 libdbus-glib-1-2 libxt6 wget
gtk2-engines-murrine gtk2-engines-pixbuf && \  
cd /opt && \  
wget
'https://download.mozilla.org/?product=firefox-46.0-SSL&os=linux64&lang=en-US'
-O firefox.tar.bz2 && \  
tar -jxvf firefox.tar.bz2 && \  
rm /opt/firefox.tar.bz2 && \  
cd && \  
wget
https://github.com/prikhi/pencil/releases/download/v2.0.21/Pencil-2.0.21-linux-
pkg.tar.gz && \  
cd / && \  
tar -zxvf /root/Pencil-2.0.21-linux-pkg.tar.gz --strip 1 && \  
mkdir /extra && \  
cd /extra && \  
wget https://github.com/nathanielw/Android-Lollipop-Pencil-
Stencils/releases/download/v1.1.0/android-lollipop-pencil-stencils-v1.1.0.zip
&& \  
wget https://github.com/nathanielw/Bootstrap-Pencil-
Stencils/releases/download/v1.1.1/bootstrap-pencil-stencils-v1.1.1.zip && \  
wget https://github.com/nathanielw/Material-Icons-for-
Pencil/releases/download/v2.0.0/material-icons-for-pencil-v2.0.0.zip && \  
wget https://github.com/DaniGuardiola/pencil-material-
template/raw/master/build/pencil-material-template-mobile.zip && \  
chmod 755 /extra && \  
useradd -m raptor  
  
ENV PATH /opt/firefox:$PATH  
ENV DISPLAY=:0  
ENV UID=1000  
ENV GID=1000  
  
CMD perl -pi -e "s/raptor:x:1000:1000/raptor:x:$UID:$GID/" /etc/passwd && \  
perl -pi -e "s/raptor:x:1000:/raptor:x:$GID:/" /etc/group  
  
USER raptor  
  
CMD ["sh", "-c", "/usr/bin/pencil"]  
  

