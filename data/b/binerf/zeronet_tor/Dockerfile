FROM ubuntu:16.04  
MAINTAINER binerf <zeronet@mygaia.org>  
  
# Base settings  
ENV DEBIAN_FRONTEND noninteractive  
ENV HOME /root  
  
# Add a specific user to run zeronet  
RUN groupadd -r -g 1000 zeronet \  
&& useradd -r -m -u 1000 -g zeronet zeronet  
  
# Update package lists  
RUN apt-get update -y  
  
# Install ZeroNet deps  
RUN apt-get install \  
msgpack-python \  
python-gevent \  
python-pip \  
python-dev \  
python-sqlalchemy \  
sudo -y  
  
RUN pip install msgpack-python --upgrade  
  
# Add Zeronet source  
ADD ./ZeroBundle/ZeroNet /home/zeronet/ZeroNet  
VOLUME /home/zeronet/ZeroNet/data  
RUN chown -R zeronet:zeronet /home/zeronet  
  
RUN echo "deb http://deb.torproject.org/torproject.org trusty main" >
/etc/apt/sources.list.d/tor.list  
RUN echo "deb-src http://deb.torproject.org/torproject.org trusty main" >>
/etc/apt/sources.list.d/tor.list  
RUN gpg --keyserver keys.gnupg.net --recv 886DDD89  
RUN gpg --export A3C4F0F979CAA22CDBA8F512EE8CBC9E886DDD89 | sudo apt-key add -  
  
# Update package lists  
RUN apt-get update -y  
# Upgrade System  
RUN apt-get -y dist-upgrade  
# Install tor application  
RUN apt-get -y install tor deb.torproject.org-keyring  
# Update tor configuration as required by zeronet  
#RUN sed -i '57 s/#//' /etc/tor/torrc  
#RUN sed -i '61 s/#//' /etc/tor/torrc  
RUN echo "ControlPort 9051" >> /usr/share/tor/tor-service-defaults-torrc  
RUN mkdir /var/run/tor  
RUN chown debian-tor. /var/run/tor  
RUN chmod 750 /var/run/tor  
# Add user to debian-tor group  
RUN usermod -a -G debian-tor zeronet  
  
ADD run.sh /run.sh  
RUN chmod 0755 /run.sh  
  
#Slimming down Docker containers  
RUN apt-get purge \  
cpp \  
build-essential \  
eject \  
g++-4.8 \  
libstdc++-4.8-dev \  
make \  
manpages \  
manpages-dev \  
vim-common \  
vim-tiny \  
-y  
RUN apt-get autoremove -y  
RUN apt-get clean -y  
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Enable password Access to UI  
RUN mv /home/zeronet/ZeroNet/plugins/disabled-UiPassword
/home/zeronet/ZeroNet/plugins/UiPassword  
# Disable stats plugin (to prevent Ddos)  
RUN mv /home/zeronet/ZeroNet/plugins/Stats
/home/zeronet/ZeroNet/plugins/disabled-Stats  
  
#Set upstart command  
CMD ["/run.sh"]  
  
#Expose ports  
EXPOSE 43110  
EXPOSE 15441  

