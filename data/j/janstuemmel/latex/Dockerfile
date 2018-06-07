FROM blang/latex  
  
MAINTAINER Jan Stümmel <info@janstuemmel.de>  
  
RUN apt-get -y update && \  
apt-get -yq install biber && \  
apt-get -yq install locales dpkg wget wput curl zip tar rsync make  
  
RUN wget
https://github.com/jgm/pandoc/releases/download/1.18/pandoc-1.18-1-amd64.deb
&& \  
dpkg -i pandoc-1.18-1-amd64.deb  
  
RUN apt-get autoclean  
RUN apt-get clean  
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
WORKDIR /data  
VOLUME ["/data"]  

