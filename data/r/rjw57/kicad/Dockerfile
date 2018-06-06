FROM ubuntu:latest  
MAINTAINER Rich Wareham <rich.kicad-docker@richwareham.com>  
  
RUN echo 'debconf debconf/frontend select Noninteractive' | \  
debconf-set-selections  
RUN apt-get -y update && apt-get -y install software-properties-common  
RUN add-apt-repository -y ppa:js-reynaud/kicad-4 && \  
apt-get -y update && apt-get -y install kicad  
  
RUN apt-get -y install xterm  
ADD run-kicad.sh /usr/bin/  
CMD [ "/usr/bin/run-kicad.sh" ]  

