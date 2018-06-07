FROM ubuntu:18.04  
LABEL maintainer "Noritaka Horio <holy.shared.design@gmail.com>"  
ARG DEBIAN_FRONTEND=noninteractive  
RUN apt -y update && \  
apt install -y --install-recommends apt-utils software-properties-common && \  
rm -rf /var/lib/apt/lists/*  
RUN apt-key adv --recv-keys --keyserver hkp://keyserver.ubuntu.com:80
0x5a16e7281be7a449 && \  
apt-key adv --recv-keys --keyserver hkp://keyserver.ubuntu.com:80
0xB4112585D386EB94  
RUN add-apt-repository "deb http://dl.hhvm.com/ubuntu $(lsb_release
-sc)-lts-3.24 main"  
RUN apt -y update && \  
apt -y --no-install-recommends install sudo curl hhvm && \  
rm -rf /var/lib/apt/lists/*  
RUN curl -sS https://getcomposer.org/installer | php  
RUN mv composer.phar /usr/local/bin/composer  

