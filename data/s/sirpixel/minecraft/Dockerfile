FROM debian:latest  
  
LABEL maintainer="pixel@happyguard.fr" \  
version=1.0 \  
description="Create a server Minecraft"  
  
RUN apt-get update \  
&& dpkg --add-architecture i386 \  
&& apt-get update \  
&& apt-get install -y mailutils postfix curl wget file bzip2 gzip unzip
bsdmainutils python util-linux ca-certificates binutils default-jdk bc tmux
lib32gcc1 libstdc++6 libstdc++6:i386 lib32z1 telnet expect sudo cron locales  
  
COPY ./*.* /  
  
RUN chmod 755 /start.sh \  
&& sed -i -e 's/\r$//' /start.sh \  
&& useradd -ms /bin/bash mcserver \  
&& echo "mcserver:mcserver" | chpasswd && adduser mcserver sudo  
  
RUN sed -i -e 's/# fr_FR.UTF-8 UTF-8/fr_FR.UTF-8 UTF-8/' /etc/locale.gen && \  
locale-gen  
ENV LANG fr_FR.UTF-8  
ENV LANGUAGE fr_FR:fr  
ENV LC_ALL fr_FR.UTF-8  
VOLUME /home/mcserver  
  
WORKDIR /home/mcserver  
  
EXPOSE 25665  
CMD ["/start.sh"]

