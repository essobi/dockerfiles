FROM ubuntu:16.04  
  
ADD https://github.com/boothj5/profanity/archive/0.5.0.tar.gz
http://www.profanity.im/install-all.sh /usr/src/  
  
RUN adduser --disabled-password profanity  
RUN apt update && apt install -y sudo unzip build-essential git automake
autoconf \  
libssl-dev libexpat1-dev libncursesw5-dev libglib2.0-dev libnotify4 libnotify-
dev libcurl3-dev \  
libxss-dev libotr5-dev libreadline-dev libtool libgpgme11-dev libgtk2.0-dev
autoconf-archive python-dev \  
libpython2.7 libgtk2.0-0 libotr5-dev libgpgme11 libxss1 \  
&& cd /usr/src && tar -xvf /usr/src/0.5.0.tar.gz \  
&& tar -xvf 0.5.0.tar.gz \  
&& cd profanity-0.5.0 \  
&& ./bootstrap.sh \  
&& bash /usr/src/install-all.sh \  
&& apt remove --purge -y unzip build-essential git automake autoconf \  
libssl-dev libexpat1-dev libncursesw5-dev libglib2.0-dev libnotify-dev
libcurl3-dev \  
libxss-dev libreadline-dev libtool libgpgme11-dev libgtk2.0-dev autoconf-
archive python-dev \  
&& apt autoremove --purge -y \  
&& rm -rf /usr/src/*  
  
USER profanity  
CMD ["profanity"]  

