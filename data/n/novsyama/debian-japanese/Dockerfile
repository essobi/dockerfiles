FROM debian:stretch  
MAINTAINER Novs Yama  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV LC_ALL ja_JP.UTF-8  
ENV LANG ${LC_ALL}  
ENV LANGUAGE ${LC_ALL}  
ENV TZ 'Asia/Tokyo'  
RUN apt-get -y update \  
&& apt-get -y install locales \  
&& apt-get -y autoclean \  
&& apt-get -y autoremove \  
&& rm -rf /var/lib/apt/lists/*  
RUN locale-gen ja_JP.UTF-8  
RUN echo ja_JP.UTF-8 UTF-8 >> /etc/locale.gen  
RUN dpkg-reconfigure -f noninteractive locales  
RUN update-locale LANG=ja_JP.UTF-8  
  
RUN echo "Asia/Tokyo" > /etc/timezone  
RUN dpkg-reconfigure -f noninteractive tzdata  
  

