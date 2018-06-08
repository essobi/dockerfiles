FROM ubuntu:14.04  
ENV DEBIAN_FRONTEND=noninteractive  
  
ENV APP_ENV="dev"  
RUN apt-get -y update && apt-get -y upgrade  
RUN apt-get install -y curl && apt-get install -y apt-transport-https  
  
RUN echo "deb http://archive.ubuntu.com/ubuntu/ trusty main restricted
universe multiverse" > /etc/apt/sources.list \  
&& echo "deb-src http://archive.ubuntu.com/ubuntu/ trusty main restricted
universe multiverse" >> /etc/apt/sources.list \  
&& echo "deb http://archive.ubuntu.com/ubuntu/ trusty-updates main restricted
universe multiverse" >> /etc/apt/sources.list \  
&& echo "deb-src http://archive.ubuntu.com/ubuntu/ trusty-updates main
restricted universe multiverse" >> /etc/apt/sources.list \  
&& echo "deb http://archive.ubuntu.com/ubuntu/ trusty-backports main
restricted universe multiverse" >> /etc/apt/sources.list \  
&& echo "deb-src http://archive.ubuntu.com/ubuntu/ trusty-backports main
restricted universe multiverse" >> /etc/apt/sources.list \  
&& echo "deb http://archive.ubuntu.com/ubuntu/ trusty-security main restricted
universe multiverse" >> /etc/apt/sources.list \  
&& echo "deb-src http://archive.ubuntu.com/ubuntu/ trusty-security main
restricted universe multiverse" >> /etc/apt/sources.list \  
&& echo "deb https://deb.nodesource.com/node_5.x trusty main" >
/etc/apt/sources.list.d/nodesource.list \  
&& echo "deb-src https://deb.nodesource.com/node_5.x trusty main" >>
/etc/apt/sources.list.d/nodesource.list  
  
RUN curl -s https://deb.nodesource.com/gpgkey/nodesource.gpg.key | apt-key add
-  
  
RUN apt-get -y update && apt-get install -y software-properties-common git  
RUN locale-gen en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LC_ALL en_US.UTF-8  
RUN apt-get upgrade -y \  
&& apt-get install -y locales sudo tzdata wget \  
&& echo "Etc/UTC" > /etc/timezone \  
&& find /var/lib/apt/lists -type f -delete \  
&& date > /.build_date  
  
RUN mkdir -p /tpl  
ADD tpl/* /tpl/  
  

