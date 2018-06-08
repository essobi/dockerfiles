FROM ubuntu:xenial  
MAINTAINER Christian Simon <simon@swine.de>  
  
# Install gramps itself  
RUN apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get -y install curl xvfb xdg-utils
python3-gi python3-gi-cairo python3-bsddb3 librsvg2-2 gir1.2-gtk-3.0 make
python3-pillow graphviz python3-pip && \  
apt-get clean && \  
rm /var/lib/apt/lists/*_*  
  
# download 4.2.3  
RUN curl -L https://github.com/gramps-
project/gramps/releases/download/v4.2.3/python3-gramps_4.2.3_all.deb >
/tmp/gramps.deb && \  
dpkg -i /tmp/gramps.deb  
  
# fix bug for around html generation  
ADD gramps_html.patch /tmp/gramps_html.patch  
RUN cd /usr/lib/python3/dist-packages/gramps/plugins/webreport/ && \  
patch < /tmp/gramps_html.patch  
  
# Generate and set default locales  
RUN locale-gen de  
ENV LANG de_DE.UTF-8  
ENV LANGUAGE de_DE  
  
RUN groupadd --gid 950 gramps && \  
useradd --gid 950 --uid 950 gramps && \  
mkdir -p /home/gramps/workdir && \  
chown -cR gramps:gramps /home/gramps/  
  
WORKDIR /home/gramps/workdir  
  
USER gramps  

