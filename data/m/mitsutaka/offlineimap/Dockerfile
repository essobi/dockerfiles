FROM ubuntu:18.04  
MAINTAINER Mitz Amano "mitsutaka.amano@gmail.com"  
ENV OFFLINEIMAP_VERSION 7.2.0  
RUN apt-get update \  
&& apt-get install -y sudo curl python git python-six make  
RUN mkdir -p /src \  
&& cd /src \  
&& curl -L
"https://github.com/OfflineIMAP/offlineimap/archive/v${OFFLINEIMAP_VERSION}.tar.gz"
\  
| tar xvz \  
&& cd offlineimap-"${OFFLINEIMAP_VERSION}" \  
&& make \  
&& python setup.py install \  
&& apt-get autoremove -y \  
&& apt-get clean \  
&& rm -rf /src* /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
VOLUME /mail  
  
CMD ["offlineimap", "-c", "/mail/offlineimaprc"]  

