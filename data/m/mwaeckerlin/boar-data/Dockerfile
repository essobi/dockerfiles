FROM mwaeckerlin/ubuntu-base  
MAINTAINER mwaeckerlin  
ENV TERM xterm  
  
ENV TIMEOUT "600"  
ENV BOAR_USER "boar"  
ENV BOAR_HOST "boar"  
ENV BOAR_PORT "22"  
ENV BOAR_REPO "boar+ssh://BOAR_USER@BOAR_HOST/boar"  
ENV BOAR_SOURCE
"https://bitbucket.org/mats_ekberg/boar/downloads/boar.16-Nov-2012.tar.gz"  
ENV LANG "en_US.UTF-8"  
ENV SSH_PUBKEY ""  
ENV SSH_PRIVKEY ""  
WORKDIR /opt  
RUN apt-get update  
RUN apt-get -y install openssh-client inotify-tools python wget mcrypt
language-pack-en  
RUN wget -O- ${BOAR_SOURCE} | tar xz  
  
ADD boar /usr/local/bin/boar  
ADD start.sh /start.sh  
WORKDIR /data  
  
RUN useradd -ms /bin/bash boar  
USER boar  
CMD /start.sh  
  
VOLUME /data  

