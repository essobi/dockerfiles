FROM ubuntu:16.04  
MAINTAINER Revolve Hosting, <admin@revolve.host>  
  
RUN apt update \  
&& apt upgrade -y \  
&& apt -y install curl software-properties-common locales git \  
&& useradd -d /home/container -m container  
  
# Ensure UTF-8  
RUN locale-gen en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LC_ALL en_US.UTF-8  
# NodeJS  
RUN curl -sL https://deb.nodesource.com/setup_6.x | bash - \  
&& apt -y install nodejs  
  
# PHP 7.1  
RUN add-apt-repository -y ppa:ondrej/php \  
&& apt update \  
&& apt -y install php7.1 php7.1-cli php7.1-gd php7.1-mysql php7.1-pdo
php7.1-mbstring php7.1-tokenizer php7.1-bcmath php7.1-xml php7.1-fpm
php7.1-curl php7.1-zip  
  
# OpenJDK 8  
RUN apt -y install openjdk-8-jdk  
  
# Python 2 & 3  
RUN apt -y install python python3  
  
# C Sharp & .NET  
RUN apt -y install mono-runtime  
  
# Lua 5.3  
RUN apt -y install lua5.3  
  
USER container  
ENV USER container  
ENV HOME /home/container  
  
WORKDIR /home/container  
  
COPY ./entrypoint.sh /entrypoint.sh  
  
CMD ["/bin/bash", "/entrypoint.sh"]  

