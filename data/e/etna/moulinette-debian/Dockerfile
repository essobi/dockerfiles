FROM debian:jessie  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get -qq update  
  
RUN apt-get install -y locales  
RUN echo "en_US.UTF-8 UTF-8" >> /etc/locale.gen  
RUN echo "fr_FR.UTF-8 UTF-8" >> /etc/locale.gen  
RUN locale-gen en_US.UTF-8 fr_FR.UTF-8  
  
ENV HOME /root  
ENV LC_ALL en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US.UTF-8  
ENV TZ Europe/Paris  
  
RUN apt-get install -y wget curl  
  
RUN echo "deb http://packages.dotdeb.org stable all" >> /etc/apt/sources.list  
RUN echo "deb-src http://packages.dotdeb.org stable all" >>
/etc/apt/sources.list  
RUN echo "deb http://packages.dotdeb.org wheezy-php55 all" >>
/etc/apt/sources.list  
RUN echo "deb-src http://packages.dotdeb.org wheezy-php55 all" >>
/etc/apt/sources.list  
RUN wget http://www.dotdeb.org/dotdeb.gpg  
RUN apt-key add dotdeb.gpg  
  
RUN apt-get -qq update  
RUN apt-get upgrade -y  
  
# piscines  
RUN apt-get install -y build-essential php5 ruby tree bc  
  
# amsg  
RUN apt-get install -y ssh host  

