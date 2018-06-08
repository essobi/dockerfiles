FROM ubuntu:latest  
  
MAINTAINER "testing" j3nnn1@nonolabs.com.uy  
  
RUN apt-get update  
  
  
# Configure the regional language settings  
  
ENV LOCALE en_US.UTF-8  
  
RUN dpkg-reconfigure locales \  
&& locale-gen ${LOCALE} \  
&& /usr/sbin/update-locale LANG=${LOCALE}  
# miscellaneous packages  
#  
RUN apt-get install --yes --no-install-recommends \  
libssl-dev \  
libcurl4-gnutls-dev \  
curl \  
wget \  
ca-certificates  
  
  
# Git command line client  
RUN apt-get install --yes git git-doc \  
&& git config \--system push.default simple  
  
# SQLite  
RUN apt-get install --yes sqlite  
  
  
  
# Create default user account  
  
ENV DST_USER nonovich  
ENV HOME /home/${DST_USER}  
RUN useradd --create-home --shell /bin/bash ${DST_USER} \  
&& echo "${DST_USER}:science" | chpasswd \  
&& mkdir ${HOME}/bin \  
&& mkdir ${HOME}/tmp  
  
  
RUN chown -R ${DST_USER}:${DST_USER} ${HOME}  
# Clean-up installation environment  
RUN apt-get clean && apt-get autoclean  
  
  
VOLUME ${HOME}  
WORKDIR ${HOME}  

