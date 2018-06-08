############  
# OS setup #  
############  
FROM ubuntu:14.04  
MAINTAINER Patrick Pedrioli  
LABEL Description="A basic wine container with support for X11 forwarding and
user matching between host-image" Version="1.0"  
  
## Let apt-get know we are running in noninteractive mode  
ENV DEBIAN_FRONTEND noninteractive  
  
## Make sure image is up-to-date  
RUN apt-get update \  
&& apt-get -y upgrade  
  
##############  
# Wine setup #  
##############  
## Enable 32 bit architecture for 64 bit systems  
RUN dpkg --add-architecture i386  
  
## Add wine repository  
RUN apt-get -y install software-properties-common \  
&& add-apt-repository ppa:wine/wine-builds \  
&& apt-get update  
  
## Install wine and winetricks  
RUN apt-get -y install --install-recommends winehq-devel cabextract  
#RUN apt-get -y install --install-recommends wine1.7  
## Setup GOSU to match user and group ids  
##  
## User: user  
## Pass: 123  
##  
## Note that this setup also relies on entrypoint.sh  
## Set LOCAL_USER_ID as an ENV variable at launch or the default uid 9001 will
be used  
## Set LOCAL_GROUP_ID as an ENV variable at launch or the default uid 250 will
be used  
## (e.g. docker run -e LOCAL_USER_ID=151149 ....)  
##  
## Initial password for user will be 123  
ENV GOSU_VERSION 1.9  
RUN set -x \  
&& apt-get update && apt-get install -y --no-install-recommends ca-
certificates wget && rm -rf /var/lib/apt/lists/* \  
&& dpkgArch="$(dpkg --print-architecture | awk -F- '{ print $NF }')" \  
&& wget -O /usr/local/bin/gosu
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$dpkgArch"
\  
&& wget -O /usr/local/bin/gosu.asc
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$dpkgArch.asc"
\  
&& export GNUPGHOME="$(mktemp -d)" \  
&& gpg --keyserver ha.pool.sks-keyservers.net --recv-keys
B42F6819007F00F88E364FD4036A9C25BF357DD4 \  
&& gpg --batch --verify /usr/local/bin/gosu.asc /usr/local/bin/gosu \  
&& rm -r "$GNUPGHOME" /usr/local/bin/gosu.asc \  
&& chmod +x /usr/local/bin/gosu \  
&& gosu nobody true  
  
ENV USER_ID 9001  
ENV GROUP_ID 250  
RUN addgroup --gid $GROUP_ID userg  
RUN useradd --shell /bin/bash -u $USER_ID -g $GROUP_ID -o -c "" -m user  
ENV HOME /home/user  
RUN chown -R user:userg $HOME  
RUN echo 'user:123' | chpasswd  
  
ENV WINEPREFIX /home/user  
## Make sure the user inside the docker has the same ID as the user outside  
COPY entrypoint.sh /usr/local/bin/entrypoint.sh  
RUN chmod 755 /usr/local/bin/entrypoint.sh  
ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]  

