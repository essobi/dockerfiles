FROM ubuntu:14.04  
MAINTAINER Hideyuki Takei <hide@soth.io>  
  
ENV HOME /root  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update && apt-get install -yq --no-install-recommends wget
software-properties-common  
  
# Add HARK repository  
RUN echo "deb http://winnie.kuis.kyoto-u.ac.jp/HARK/harkrepos trusty non-
free\ndeb-src http://winnie.kuis.kyoto-u.ac.jp/HARK/harkrepos trusty non-free"
> \  
/etc/apt/sources.list.d/hark.list  
RUN wget -q -O - http://winnie.kuis.kyoto-u.ac.jp/HARK/harkrepos/public.gpg |
sudo apt-key add -  
RUN add-apt-repository ppa:chris-lea/node.js  
  
RUN apt-get update  
RUN apt-get install -yq --no-install-recommends supervisor  
RUN apt-get install -yq --no-install-recommends vim-tiny alsa-utils  
RUN apt-get install -yq --no-install-recommends xfce4 xfce4-goodies  
RUN apt-get install -yq --no-install-recommends x11vnc xvfb  
RUN apt-get install -yq nodejs harkfd hark-binaural hark-designer
julius-4.2.3-hark-plugin harktool4  
RUN apt-get autoclean \  
&& apt-get autoremove \  
&& rm -rf /var/lib/apt/lists/*  
  
# Change hark setting  
#RUN sed -i 's/sudo\ forever\ start\ app\\.js/sudo\ forever\ start\ app\\.js\
allowremote/g' /usr/bin/hark_designer  
RUN cd /usr/bin/hark-designer && npm install  
  
WORKDIR /usr/share/hark-designer/userdata/networks  
  
ADD scripts/startup.sh /root/startup.sh  
ADD config/supervisord.conf /root/supervisord.conf  
ADD config/.vimrc /root/.vimrc  
ADD config/julius /root/julius  
  
EXPOSE 5900  
EXPOSE 3000  
VOLUME /usr/share/hark-designer/userdata/networks  
  
ENTRYPOINT ["bash", "/root/startup.sh"]  
  

