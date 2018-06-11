FROM ubuntu:16.04  
MAINTAINER watsy0007@gmail.com  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV LANGUAGE en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LC_ALL en_US.UTF-8  
ENV TZ Asia/Shanghai  
RUN locale-gen $LANGUAGE && \  
dpkg-reconfigure locales && \  
dpkg-reconfigure -f noninteractive tzdata && \  
ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone  
  
RUN apt-get update && apt-get upgrade -y && apt-get install ruby2.3
ruby2.3-dev software-properties-common -y && apt-get clean && \  
rm -rf /usr/share/doc/* && \  
rm -rf /usr/share/locale/* && \  
rm -rf /usr/share/man/* && \  
rm -rf /var/cache/debconf/*-old && \  
rm -rf /var/lib/apt/lists/*  
  
RUN rm /bin/sh && ln -s /bin/bash /bin/sh  
  
CMD ["bin/bash"]  

