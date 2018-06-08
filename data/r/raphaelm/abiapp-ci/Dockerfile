FROM debian:jessie  
MAINTAINER raphael@abiapp.net  
  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get update && apt-get install -y python python-dev wget \  
libmysqlclient-dev python-virtualenv npm build-essential git rrdtool locales \  
libcairo2-dev libpango1.0-dev libglib2.0-dev libxml2-dev libxslt1-dev librrd-
dev \  
texlive-latex-recommended texlive-latex-extra texlive-xetex texlive-lang-
german \  
libjpeg-dev libfreetype6 libfreetype6-dev zlib1g-dev libssl-dev \  
libsqlite3-0 libsqlite3-dev libreadline-dev libncurses5-dev libgdbm-dev \  
memcached nginx graphicsmagick libmemcached-dev libfontconfig bzip2  
  
RUN npm install -g less@2.5.0  
RUN ln -s /usr/bin/nodejs /usr/bin/node  
RUN ln -s /node_modules/.bin/lessc /usr/bin/lessc  
  
RUN locale-gen  
RUN update-locale LANG=C.UTF-8  
ENV LC_ALL C.UTF-8  
ENV LANG C.UTF-8  
RUN apt-get clean && rm -rf /var/lib/apt/lists/*  
  
# Get Python 3  
RUN wget https://www.python.org/ftp/python/3.6.0/Python-3.6.0.tgz && \  
tar xvf Python-3.6.0.tgz && \  
cd Python-3.6.0 && \  
./configure --enable-optimizations && \  
make -j4 && \  
make altinstall  
  
# We want a current pip  
ADD get-pip.py /tmp/get-pip.py  
RUN python /tmp/get-pip.py  
  
ENV PHANTOMJS_VERSION 1.9.7  
# Commands  
RUN \  
mkdir -p /srv/var && \  
wget -q -O /tmp/phantomjs-$PHANTOMJS_VERSION-linux-x86_64.tar.bz2
https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-$PHANTOMJS_VERSION-
linux-x86_64.tar.bz2 && \  
tar -xjf /tmp/phantomjs-$PHANTOMJS_VERSION-linux-x86_64.tar.bz2 -C /tmp && \  
rm -f /tmp/phantomjs-$PHANTOMJS_VERSION-linux-x86_64.tar.bz2 && \  
mv /tmp/phantomjs-$PHANTOMJS_VERSION-linux-x86_64/ /srv/var/phantomjs && \  
ln -s /srv/var/phantomjs/bin/phantomjs /usr/bin/phantomjs  
  
CMD ["/bin/bash"]  

