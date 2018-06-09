FROM debian:latest  
  
LABEL maintainer="pixel@happyguard.fr" \  
version=1.0 \  
description="Create a server cs1.6"  
  
RUN apt-get update \  
&& dpkg --add-architecture i386 \  
&& apt-get update \  
&& apt-get install -y mailutils postfix curl wget file bzip2 gzip unzip
bsdmainutils python util-linux ca-certificates binutils bc tmux lib32gcc1
libstdc++6 libstdc++6:i386 lib32z1 telnet expect sudo cron locales  
  
COPY ./*.* /  
  
RUN chmod 755 /start.sh \  
&& sed -i -e 's/\r$//' /start.sh \  
&& useradd -ms /bin/bash csserver \  
&& echo "csserver:csserver" | chpasswd && adduser csserver sudo  
  
RUN sed -i -e 's/# fr_FR.UTF-8 UTF-8/fr_FR.UTF-8 UTF-8/' /etc/locale.gen && \  
locale-gen  
ENV LANG fr_FR.UTF-8  
ENV LANGUAGE fr_FR:fr  
ENV LC_ALL fr_FR.UTF-8  
VOLUME /home/csserver  
  
USER csserver  
  
WORKDIR /home/csserver  
  
EXPOSE 27015 27020 27005 27015/udp 27020/udp 27005/udp  
  
CMD ["/start.sh"]

