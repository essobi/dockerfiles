FROM debian:latest  
  
LABEL maintainer="pixel@rageclic.fr" \  
version=1.0 \  
description="Create a server HurtWorld"  
  
RUN apt-get update \  
&& dpkg --add-architecture i386 \  
&& apt-get update \  
&& apt-get install -y mailutils postfix curl wget file bzip2 gzip unzip
binutils bsdmainutils python util-linux ca-certificates tmux lib32gcc1
libstdc++6 libstdc++6:i386 expect sudo  
  
COPY ./*.* /  
  
RUN chmod 755 /start.sh \  
&& sed -i -e 's/\r$//' /start.sh \  
&& useradd -ms /bin/bash hwserver \  
&& echo "hwserver:hwserver" | chpasswd && adduser hwserver sudo  
  
VOLUME /home/hwserver  
  
USER hwserver  
  
WORKDIR /home/hwserver  
  
EXPOSE 12871 13871 12881 12871/udp 13871/udp 12881/udp  
  
CMD ["/start.sh"]  

