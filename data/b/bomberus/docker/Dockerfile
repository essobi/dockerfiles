FROM debian:jessie  
#ARG pass  
MAINTAINER Pascal Maximilian Bremer <mail at pmbremer.de>  
ENV DEBIAN_FRONTEND noninteractive  
RUN REPO=http://cdn-fastly.deb.debian.org && \  
echo "deb $REPO/debian jessie main contrib non-free\n \  
deb $REPO/debian-security jessie/updates main contrib non-free\n \  
deb http://ftp2.de.debian.org/debian testing main contrib non-free\n \  
deb $REPO/debian experimental main contrib non-free" > /etc/apt/sources.list
&& \  
echo "deb http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main" | tee
/etc/apt/sources.list.d/webupd8team-java.list && \  
echo "deb-src http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main" |
tee -a /etc/apt/sources.list.d/webupd8team-java.list && \  
echo "deb http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main" | tee
/etc/apt/sources.list.d/webupd8team-java.list && \  
echo "deb-src http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main" |
tee -a /etc/apt/sources.list.d/webupd8team-java.list && \  
apt-key adv --keyserver keyserver.ubuntu.com \--recv-keys EEA14886 && \  
apt-get -y update && \  
apt-get -y install npm nodejs nodejs-legacy wget locales git python-matplotlib
inkscape libxml2-dev libxslt-dev zsh vim htop && \  
/usr/sbin/update-locale LANG=C.UTF-8 && \  
echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true |
/usr/bin/debconf-set-selections && \  
apt-get -y install oracle-java8-installer && \  
apt-get -y -t testing install libstdc++6 && \  
apt-get -y -t experimental install libicu58 && \  
locale-gen C.UTF-8 && \  
apt-get remove -y locales && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
ENV LANG C.UTF-8  
ENV NLTK_DATA_ROOT /opt/nltk_data  
ENV PATH=/opt/conda/bin:$PATH  
RUN npm install -g configurable-http-proxy && \  
useradd --create-home --shell /bin/bash retkowski  
# echo "retkowski:$pass" | chpasswd  
  
#VOLUME ["/opt/conda"]  
#VOLUME ["/opt/nltk_data"]  
  
ADD ./bin /usr/sbin  
RUN chmod a+x /usr/sbin/*  
  
RUN mkdir /opt/conda && mkdir /opt/nltk_data  
  
RUN mkdir -p /srv/jupyterhub  
WORKDIR /srv/jupyterhub/  
EXPOSE 8000  
LABEL org.jupyter.service="jupyterhub"  
CMD ["jupyterhub --no-ssl"]  

