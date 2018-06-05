# ----------------------------------  
# Pterodactyl Core Dockerfile  
# Environment: Source Engine  
# Minimum Panel Version: 0.6.0  
# ----------------------------------  
FROM ubuntu:16.04  
ENV DEBIAN_FRONTEND noninteractive  
# Install Dependencies  
RUN dpkg --add-architecture i386 \  
&& apt-get update \  
&& apt-get upgrade -y \  
&& apt-get install -y tar curl wget gcc g++ software-properties-common apt-
transport-https expect gettext zip unzip git php php-zip php-cli php-bcmath
php-bz2 php-json php-simplexml php-sockets lib32gcc1 lib32tinfo5 lib32z1
lib32stdc++6 libtinfo5:i386 libncurses5:i386 libcurl3-gnutls:i386 iproute2 gdb
libsdl1.2debian libfontconfig \  
&& apt-get clean \  
&& apt-get autoclean \  
&& useradd -m -d /home/container container  
  
COPY ./getcomposer.sh ./getcomposer.sh  
RUN chmod +x ./getcomposer.sh  
RUN ./getcomposer.sh  
RUN mv ./composer.phar /usr/local/bin/composer  
  
USER container  
ENV HOME /home/container  
WORKDIR /home/container  
  
RUN touch ./composer.json \  
&& echo '{"require": {} }' > ./composer.json \  
&& composer require monolog/monolog koraktor/steam-condenser  
  
COPY ./rcon ./rcon  
COPY ./entrypoint.sh /entrypoint.sh  
CMD ["/bin/bash", "/entrypoint.sh"]

