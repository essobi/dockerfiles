FROM debian:8  
MAINTAINER Dominique Barton  
  
#  
# Create user and group for SickRage.  
#  
RUN groupadd -r -g 666 sickrage \  
&& useradd -r -u 666 -g 666 -d /sickrage sickrage  
  
#  
# Add SickRage init script.  
#  
ADD sickrage.sh /sickrage.sh  
RUN chmod 755 /sickrage.sh  
  
#  
# Install SickRage and all required dependencies.  
#  
RUN export VERSION=v2017.06.05-1 \  
&& apt-get -q update \  
&& apt-get install -qy curl ca-certificates locales python-setuptools build-
essential python-dev libssl-dev libxml2-dev libxslt-dev \  
&& sed -i 's/^# \\(en_GB\\.UTF-8.*\\)$/\1/' /etc/locale.gen \  
&& locale-gen en_GB.UTF-8 \  
&& easy_install pip \  
&& curl -o /tmp/sickrage.tar.gz
https://codeload.github.com/SickRage/SickRage/tar.gz/${VERSION} \  
&& tar xzf /tmp/sickrage.tar.gz \  
&& mv SickRage-* sickrage \  
&& chown -R sickrage: sickrage \  
&& pip install lxml pyOpenSSL \  
&& apt-get -y remove curl build-essential python-dev libssl-dev libxml2-dev
libxslt-dev \  
&& apt-get -y autoremove \  
&& apt-get -y clean \  
&& rm -rf /var/lib/apt/lists/* \  
&& rm -rf /tmp/*  
  
#  
# Define container settings.  
#  
ENV ENV LANG en_GB.UTF-8  
ENV LANGUAGE en_GB:en  
ENV LC_ALL en_GB.UTF-8  
VOLUME ["/datadir", "/media"]  
  
EXPOSE 8081  
#  
# Start SickRage.  
#  
WORKDIR /sickrage  
  
CMD ["/sickrage.sh"]  

