# Created on Mar. 8, 2017  
# @author: Yvictor  
FROM ubuntu:16.04  
MAINTAINER yvictor  
  
ENV LANG=C.UTF-8 LC_ALL=C.UTF-8  
RUN apt-get update --fix-missing && apt-get install -y curl git make bzip2  
  
#RUN apt-get update --fix-missing && apt-get install -y make g++ wget bzip2
ca-certificates \  
#libglib2.0-0 libxext6 libsm6 libxrender1 \  
#git mercurial subversion  
ENV PYENV_ROOT /root/.pyenv  
ENV PATH
/root/.pyenv/shims:/root/.pyenv/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin  
RUN curl -L https://raw.githubusercontent.com/yyuu/pyenv-
installer/master/bin/pyenv-installer | bash  
RUN pyenv install miniconda2-4.1.11  
RUN pyenv global miniconda2-4.1.11  
  
# change to use pyenv to management python env  
# RUN curl -L https://raw.githubusercontent.com/yyuu/pyenv-
installer/master/bin/pyenv-installer | bash  
# miniconda2-4.1.11  
### tor part  
RUN apt-get -qq install --yes build-essential libevent-dev libssl-dev curl g++  
# install tor  
ENV TOR_VERSION 0.2.9.14  
RUN curl -0 -L https://dist.torproject.org/tor-${TOR_VERSION}.tar.gz | tar xz
-C /tmp  
RUN cd /tmp/tor-${TOR_VERSION} && ./configure  
RUN cd /tmp/tor-${TOR_VERSION} && make -j 4  
RUN cd /tmp/tor-${TOR_VERSION} && make install  
  
# install delegate  
ENV DELEGATE_VERSION 9.9.13  
RUN curl
ftp://anonymous@ftp.delegate.org/pub/DeleGate/delegate${DELEGATE_VERSION}.tar.gz
| tar xz -C /tmp  
RUN echo "ADMIN=root@root.com" >
/tmp/delegate${DELEGATE_VERSION}/src/DELEGATE_CONF  
RUN sed -i -e '1i#include <util.h>\'
/tmp/delegate${DELEGATE_VERSION}/maker/_-forkpty.c  
RUN cd /tmp/delegate${DELEGATE_VERSION} && make  
  
# install haproxy  
ENV HAPROXY_VERSION 1.6.8  
RUN curl -0 -L
http://haproxy.1wt.eu/download/1.6/src/haproxy-${HAPROXY_VERSION}.tar.gz | tar
xz -C /tmp  
RUN cd /tmp/haproxy-${HAPROXY_VERSION}/ && make TARGET=linux2628 USE_OPENSSL=1
USE_ZLIB=1  
RUN cd /tmp/haproxy-${HAPROXY_VERSION}/ && make install  
ADD ./haproxy.conf /etc/default/haproxy.conf  
  
# prepare tor folders  
RUN mkdir -p /var/db/tor/1 /var/db/tor/2 /var/db/tor/3 /var/db/tor/4
/var/db/tor/5 /var/db/tor/6 /var/db/tor/7 /var/db/tor/8 /var/db/tor/9
/var/db/tor/10  
RUN chmod -R 700 /var/db/tor  
ADD start.sh /  
RUN chmod +x /start.sh  
ADD ./torrc /usr/local/etc/tor/torrc  
  
EXPOSE 9100 9101 2090 53  
# CMD ["./start.sh"]  
RUN apt-get install -y curl grep sed dpkg git xvfb firefox && \  
TINI_VERSION=`curl https://github.com/krallin/tini/releases/latest | grep -o
"/v.*\"" | sed 's:^..\\(.*\\).$:\1:'` && \  
curl -L
"https://github.com/krallin/tini/releases/download/v${TINI_VERSION}/tini_${TINI_VERSION}.deb"
> tini.deb && \  
dpkg -i tini.deb && \  
rm tini.deb && \  
apt-get clean  
  
ADD
https://github.com/mozilla/geckodriver/releases/download/v0.12.0/geckodriver-v0.12.0-linux64.tar.gz
/usr/local/bin/  
WORKDIR /usr/local/bin/  
RUN tar -xvf geckodriver-v0.12.0-linux64.tar.gz && \  
rm geckodriver-v0.12.0-linux64.tar.gz  
  
#RUN wget --quiet -O ~/geckodriver.tar.gz && \  
#tar -xvf ~/geckodriver.tar.gz  
#rm ~/geckodriver.tar.gz \  
#mv ~/geckodriver /bin/geckodriver  
#RUN curl
"https://gist.githubusercontent.com/amberj/6695353/raw/d7d981379c9602e6323d09a90d6a84cd3e3177a2/setup-
headless-selenium-xvfb.sh"  
#/bin/bash setup-headless-selenium-xvfb.sh  
WORKDIR /home  
# RUN conda config --set auto_update_conda False  
RUN conda install -c anaconda beautifulsoup4 lxml=3.7.0 -y  
RUN pip install selenium beautifulsoup4 xvfbwrapper PyVirtualDisplay requests
pyquery pymongo python-amazon-mws celery raven  
  
CMD [ "/bin/bash" ]  
  
COPY . /docker-crawlerbase  
WORKDIR /docker-crawlerbase  
  
RUN /bin/bash /start.sh & python test.py  
  
WORKDIR /home  
#RUN rm -r -f /docker-crawlerbase  
ENTRYPOINT ["/start.sh"]  

