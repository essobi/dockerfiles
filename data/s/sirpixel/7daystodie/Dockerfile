FROM debian:latest  
  
LABEL maintainer="pixel@rageclic.fr" \  
version=1.0 \  
description="Create a server 7 Days To Die"  
  
RUN apt-get update \  
&& dpkg --add-architecture i386 \  
&& apt-get update \  
&& apt-get install -y mailutils postfix curl wget file bzip2 gzip unzip
bsdmainutils python util-linux ca-certificates binutils bc tmux lib32gcc1
libstdc++6 libstdc++6:i386 lib32z1 telnet expect sudo cron locales  
  
COPY ./*.* /  
  
RUN chmod 755 /start.sh \  
&& sed -i -e 's/\r$//' /start.sh \  
&& useradd -ms /bin/bash sdtdserver \  
&& echo "sdtdserver:sdtdserver" | chpasswd && adduser sdtdserver sudo \  
&& echo "* * * * * sdtdserver /home/sdtdserver/sdtdserver monitor > /dev/null
2>&1" >> /etc/cron.d/sdtdserver-restart \  
&& chmod 0644 /etc/cron.d/sdtdserver-restart \  
&& cron  
  
RUN sed -i -e 's/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/' /etc/locale.gen && \  
locale-gen  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8  
VOLUME /home/sdtdserver  
  
WORKDIR /home/sdtdserver  
  
EXPOSE 26900 8080-8082 26900/udp 26900-26902/udp  
  
CMD ["/start.sh"]

