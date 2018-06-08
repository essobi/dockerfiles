FROM ubuntu:16.04  
LABEL maintainer="Bernd Doser <bernd.doser@braintwister.eu>"  
  
# Install dependencies  
RUN apt-get update \  
&& apt-get -y install \  
gir1.2-gexiv2-0.10 \  
gir1.2-gtk-3.0 \  
gir1.2-osmgpsmap-1.0 \  
graphviz \  
librsvg2-2 \  
python3-bsddb3 \  
python3-gi \  
python3-gi-cairo \  
python3-pillow \  
python3-pip \  
xdg-utils \  
xvfb \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
ADD https://github.com/gramps-
project/gramps/releases/download/v4.2.8/python3-gramps_4.2.8_all.deb
/tmp/gramps.deb  
RUN dpkg -i /tmp/gramps.deb \  
&& rm /tmp/gramps.deb  
  
CMD gramps  

