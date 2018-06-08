#-------------------------------------------------------------------------------  
#  
# WARNING! WARNING! WARNING!  
# THIS IMAGE IS BEING BUILT PUBLICLY  
# DO NOT ADD PRODUCTION SECRETS HERE  
#  
#-------------------------------------------------------------------------------  
FROM ubuntu:16.04  
# package install preflight (external dependencies and hacks)  
RUN echo "deb http://us-west-2.ec2.archive.ubuntu.com/ubuntu/ xenial
multiverse" >> /etc/apt/sources.list.d/multiverse.list \  
&& apt-get update \  
&& apt-get install --no-install-suggests -y cabextract curl fontconfig \  
&& ( \  
FONTS=arial,arialb,times \  
&& cd /tmp && curl --remote-name-all -L
http://downloads.sourceforge.net/corefonts/{$FONTS}32.exe \  
&& /bin/bash -c "cabextract -d /usr/share/fonts/truetype/msttcorefonts
/tmp/{$FONTS}32.exe && rm /tmp/{$FONTS}32.exe" \  
) \  
&& curl -sL https://deb.nodesource.com/setup_7.x | bash -  
  
# install apt packages  
RUN apt-get install --no-install-suggests -y \  
build-essential \  
nodejs \  
ruby2.3 \  
ruby2.3-dev \  
libxml2-dev \  
libmysqlclient-dev \  
libmagick++-dev \  
imagemagick \  
libsqlite3-dev \  
sqlite3 \  
git-core \  
locales \  
tzdata \  
&& rm -rf /var/lib/apt/lists/* \  
&& echo 'gem: --no-document' > /etc/gemrc \  
&& gem install bundler \  
&& locale-gen en_US.UTF-8  
  
ENV LANG=en_US.UTF-8 \  
LANGUAGE=en_US:en \  
LC_ALL=en_US.UTF-8  

