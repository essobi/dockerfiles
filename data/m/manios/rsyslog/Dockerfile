FROM ubuntu:16.04  
ENV DEBIAN_FRONTEND=noninteractive  
  
LABEL name="Rsyslog" \  
version="8.34.0" \  
homepage="http://rsyslog.com" \  
maintainer="Christos Manios <maniopaido@gmail.com>"  
# Copied from
https://github.com/voxxit/dockerfiles/blob/master/rsyslog/Dockerfile  
# Enhancement for libraries from https://github.com/rsyslog/rsyslog-pkg-ubuntu  
# Structure from: https://github.com/camptocamp/docker-rsyslog-bin  
#  
# We use Ubuntu 16.04 on purpose because  
# newer versions do not have liblogging-stdlog0 package  
  
  
COPY /start.sh /usr/sbin/start-rsyslog  
COPY /lognorm.sh /usr/sbin/lognorm  
  
RUN apt-get update \  
&& apt-get install -y software-properties-common \  
&& add-apt-repository ppa:adiscon/v8-stable \  
&& add-apt-repository ppa:maxmind/ppa \  
&& apt-get update \  
&& apt-get install -y -f sudo \  
curl \  
vim \  
htop \  
netcat \  
net-tools \  
logrotate \  
libfastjson4 \  
liblogging-stdlog0 \  
rsyslog \  
rsyslog-doc \  
rsyslog-elasticsearch \  
rsyslog-imptcp \  
rsyslog-mmanon \  
rsyslog-mmfields \  
rsyslog-mmjsonparse \  
rsyslog-mmnormalize \  
rsyslog-mmrm1stspace \  
rsyslog-mmutf8fix \  
rsyslog-relp \  
rsyslog-utils \  
libmaxminddb0 \  
libmaxminddb-dev \  
mmdb-bin \  
&& ln -s /usr/lib/lognorm/lognormalizer /usr/sbin/lognormalizer \  
&& echo "set number" | tee -a /etc/vim/vimrc \  
&& apt-get -y --purge --autoremove remove software-properties-common \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* \  
&& chmod 755 /usr/sbin/start-rsyslog \  
&& chmod 755 /usr/sbin/lognorm \  
&& update-rc.d -f rsyslog remove \  
&& echo "Configuring VIM" \  
&& echo "set number" | tee -a /etc/vim/vimrc \  
&& echo "syntax on" | tee -a /etc/vim/vimrc \  
&& echo "colorscheme evening" | tee -a /etc/vim/vimrc  
  
EXPOSE 514 514/udp  
  
VOLUME [ "/var/log", "/etc/rsyslog.d" ]  
  
CMD ["start-rsyslog"]  

