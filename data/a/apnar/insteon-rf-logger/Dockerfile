FROM ubuntu:xenial  
MAINTAINER Josh Lukens <jlukens@botch.com>  
  
ENV LANG C.UTF-8  
ENV DEBIAN_FRONTEND noninteractive  
  
ENV DEBIAN_FRONTEND noninteractive  
  
USER root  
  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8  
RUN apt-get update -y -qq && \  
apt-get dist-upgrade -y && \  
apt-get install -y --no-install-recommends locales && \  
locale-gen en_US.UTF-8 && \  
  
apt-get install -y --no-install-recommends ca-certificates wget sdcc git
python-usb && \  
  
mkdir /insteon && \  
cd /insteon && \  
wget https://bitbucket.org/atlas0fd00m/rfcat/downloads/rfcat_150225.tgz && \  
tar xvfz rfcat_150225.tgz && \  
rm -f rfcat_150225.tgz && \  
ln -s rfcat_150225 rfcat && \  
git clone https://github.com/apnar/insteonrf.git insteonrf && \  
  
cd /insteon/rfcat && \  
python setup.py install && \  
  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
VOLUME /data  
  
COPY entrypoint.sh /entrypoint.sh  
RUN chmod 755 /entrypoint.sh  
ENTRYPOINT ["/entrypoint.sh"]  
  

