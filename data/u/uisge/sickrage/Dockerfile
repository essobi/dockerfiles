FROM phusion/baseimage:0.9.19  
MAINTAINER https://github.com/uisge-beatha  
ENV DEBIAN_FRONTEND noninteractive  
  
######################################  
## Environment  
######################################  
ENV DEBIAN_FRONTEND noninteractive  
ENV LC_ALL en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US.UTF-8  
######################################  
# Set correct environment variables  
######################################  
ENV HOME /root  
  
# Use baseimage-docker's init system  
CMD ["/sbin/my_init"]  
  
######################################  
## Configure Directories  
######################################  
## SickRage configuration folder  
VOLUME /SickRage-config  
  
## SickRage watched folder  
VOLUME /watched  
  
## Downloads  
VOLUME /downloads  
  
## SSL keys & certs  
VOLUME /certs  
  
## media  
VOLUME /media  
  
RUN mkdir -p /files /home/ashtaroth  
  
######################################  
## Upgrade OS  
######################################  
RUN apt-get update -q && apt-get upgrade -y -o Dpkg::Options::="--force-
confold"  
  
######################################  
## SickRage setup  
######################################  
#Python 2.7 Prerequisites  
RUN add-apt-repository -y "deb http://us.archive.ubuntu.com/ubuntu/ xenial
multiverse"  
RUN add-apt-repository -y "deb http://us.archive.ubuntu.com/ubuntu/ xenial-
updates multiverse"  
RUN apt-get update -qq  
RUN apt-get install -qy build-essential checkinstall git  
RUN apt-get install -qy libreadline-gplv2-dev libncursesw5-dev libssl-dev tk-
dev libgdbm-dev libc6-dev libbz2-dev libffi-dev libxslt1-dev libxslt1.1
libxml2-dev libxml2 avahi-daemon avahi-utils  
  
#Download sqlite3  
RUN curl -L https://www.sqlite.org/2016/sqlite-autoconf-3110100.tar.gz -o
/sqlite-autoconf-3110100.tar.gz  
  
#Verify sqlite3  
ADD sqlite3-sha1sum.txt /sqlite3-sha1sum.txt  
RUN sha1sum --check /sqlite3-sha1sum.txt  
  
#Extract and build sqlite3 3.11  
RUN tar xf /sqlite-autoconf-3110100.tar.gz  
RUN cd /sqlite-autoconf-3110100 && ./configure && make && make install
install-includeHEADERS  
  
#Cleanup sqlite3  
RUN rm /sqlite3-sha1sum.txt  
RUN rm /sqlite-autoconf-3110100.tar.gz  
RUN rm -rf /sqlite-autoconf-3110100  
  
#Download Python 2.7  
RUN curl -L https://www.python.org/ftp/python/2.7.10/Python-2.7.10.tar.xz -o
/Python-2.7.10.tar.xz  
  
#Verify the Python 2.7 download  
ADD python-md5sum.txt /python-md5sum.txt  
RUN md5sum --check /python-md5sum.txt  
  
#Extract and build Python 2.7  
RUN tar xf /Python-2.7.10.tar.xz  
RUN cd /Python-2.7.10 && ./configure && make altinstall  
  
#Cleanup Python 2.7  
RUN rm /python-md5sum.txt  
RUN rm /Python-2.7.10.tar.xz  
RUN rm -rf /Python-2.7.10  
  
#Install PIP  
RUN curl -L https://bootstrap.pypa.io/get-pip.py -o /get-pip.py  
RUN python2.7 /get-pip.py  
RUN rm /get-pip.py  
  
RUN apt-get install -qy git  
RUN pip2.7 install pyopenssl #==0.13.1  
  
#Install SickRage  
RUN git clone https://github.com/SickRage/SickRage.git /opt/sickrage  
#RUN pip2.7 install -r /opt/sickrage/sickrage/requirements.txt  
#Add Scripts  
RUN git clone https://github.com/nzbget/FailureLink.git /NZBGet-
config/ppscripts/FailureLink  
RUN git clone https://github.com/nzbget/VideoSort.git /NZBGet-
config/ppscripts/VideoSort  
RUN git clone https://github.com/clinton-hall/GetScripts.git /NZBGet-
config/ppscripts/GetScripts  
  
#Add Base .ini file  
ADD config.ini /SickRage-config.ini  
ADD sickrage.sh /sickrage.sh  
  
#DBUS requires this directory  
RUN mkdir -p /var/run/dbus  
VOLUME /var/run/dbus  
#Configure Avahi  
ADD avahi-daemon.conf /etc/avahi/avahi-daemon.conf  
  
VOLUME /config  
VOLUME /data  
VOLUME /downloads  
  
######################################  
## Expose Ports  
######################################  
## SickRage  
EXPOSE 8081  
######################################  
## Add Services to runit  
######################################  
## Add SickRage  
RUN mkdir /etc/service/SickRage  
ADD sickrage.sh /etc/service/SickRage/run  
RUN chmod +x /etc/service/SickRage/run  
  
# Add initd.sh to execute during container startup  
ADD initd.sh /etc/my_init.d/initd.sh  
RUN chmod +x /etc/my_init.d/initd.sh  
  
######################################  
## Clean up APT when done.  
######################################  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

