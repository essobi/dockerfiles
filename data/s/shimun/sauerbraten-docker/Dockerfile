FROM ubuntu:xenial  
MAINTAINER Robert Jacob <xperimental@solidproject.de>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update \  
&& apt-get install -y libx11-6 libsdl1.2debian libsdl-mixer1.2 libsdl-image1.2
libgl1-mesa-glx bzip2 wget \  
&& apt-get clean  
  
RUN wget -qO /usr/local/sauerbraten.tar.bz2 "https://10gbps-
io.dl.sourceforge.net/project/sauerbraten/sauerbraten/2013_01_04/sauerbraten_2013_02_03_collect_edition_linux.tar.bz2"
\  
&& cd /usr/local/ \  
&& tar xvjf /usr/local/sauerbraten.tar.bz2 \  
&& rm /usr/local/sauerbraten.tar.bz2 \  
&& chown -R root:root /usr/local/sauerbraten  
  
RUN wget -qO /usr/local/bin/dumb-init https://github.com/Yelp/dumb-
init/releases/download/v1.1.1/dumb-init_1.1.1_amd64 \  
&& chmod +x /usr/local/bin/dumb-init  
  
VOLUME /root/.sauerbraten/  
  
WORKDIR /usr/local/sauerbraten/  
  
EXPOSE 28784/udp 28785/udp 28786/udp  
  
CMD [ "/usr/local/bin/dumb-init", "./sauerbraten_unix", "-d" ]  

