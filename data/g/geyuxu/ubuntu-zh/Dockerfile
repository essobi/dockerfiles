FROM ubuntu:14.04  
RUN apt-get install -y locales  
WORKDIR /usr/share/locales  
RUN ./install-language-pack en_US.UTF-8  
RUN dpkg-reconfigure locales  
RUN export LC_ALL=en_US.UTF-8  
RUN echo "export LC_ALL=en_US.UTF-8" >> /etc/bash.bashrc  
  
WORKDIR /root  
  
ADD ./alisource /etc/apt/sources.list  
  

