FROM ubuntu:12.04.5  
  
MAINTAINER lient  
  
RUN apt-get update && apt-get install -y util-linux lib32z1-dev lib32bz2-dev
g++-multilib gcc-multilib libc6-dev mesa-common-dev libssl-dev libx11-dev
xlibmesa-glu-dev libsqlite3-0 mscgen libwww-mechanize-perl libcr-dev texlive-
fonts-recommended texlive-latex-extra cpp g++ g++-4.6-multilib cpp-4.6 g++-4.6
g++-4.6 gcc-4.6 gcc-multilib make libmysqlclient-dev libxml2-dev libbison-dev
flex libxcrypt-dev libmagick++-dev libreadline6-dev libmagickcore-dev
libmagickwand-dev librsvg2-dev \  
libgtk2.0-dev libxi-dev libxcursor-dev libxfixes-dev libxcomposite-dev
libxdamage-dev libdbd-sqlite3-perl libaprutil1-dev uuid-dev libapr1-dev rsync
python python-dev python-distribute python-pip unzip zip perlmagick perl-
modules liblwp-mediatypes-perl libpng12-0 vim libdbd-mysql-perl libstring-
crc32-perl pngcrush pngquant optipng iputils-ping libdatetime-perl cron
imagemagick gawk tree htop tcptraceroute && \  
apt-get purge -y texlive* && apt-get autoremove -y && apt-get clean && rm -rf
/var/lib/apt/lists/*  
  
COPY requirements.txt /tmp/requirements.txt  
RUN pip install -r /tmp/requirements.txt  
  
RUN cp /etc/apt/sources.list /etc/apt/sources.list.bak && echo "deb
http://archive.ubuntu.com/ubuntu precise main universe" >
/etc/apt/sources.list  
RUN apt-get update && apt-get install -y perl cpanminus && apt-get clean && rm
-rf /var/lib/apt/lists/*  
RUN cpanm -v Net::LDAP String::CRC32  
RUN mv /etc/apt/sources.list.bak /etc/apt/sources.list && locale-gen en_US  
  
COPY NK_POI_1.* /home/nds/keystore/  
COPY genRootFS.sh /  
COPY p4 /usr/bin/  
  
## for ATS binary  
RUN apt-get update && apt-get install -y libboost-dev libx11-dev:i386
libxml2:i386 --no-install-recommends &&\  
apt-get autoremove -y && apt-get clean && rm -rf /var/lib/apt/lists/* &&\  
ln -s /usr/lib/i386-linux-gnu/libxml2.so.2.7.8 /usr/lib/i386-linux-
gnu/libxml2.so  

