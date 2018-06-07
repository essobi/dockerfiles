FROM debian:wheezy  
  
MAINTAINER y_uuki y_uuki@hatena.ne.jp  
  
ENV DEBIAN_FRONTEND noninteractive  
RUN \  
apt-get update && \  
apt-get install -y build-essential git curl supervisor libreadline-dev zlib1g
zlib1g-dev libbz2-dev libsqlite3-dev libssl-dev && \  
rm -fr /var/lib/apt/lists/*  
  
ENV PATH /opt/python/bin:/usr/local/bin:$PATH  
  
# install python  
RUN \  
git clone git://github.com/yyuu/pyenv.git && \  
cd pyenv/plugins/python-build && \  
./install.sh  
RUN python-build 2.7.6 /opt/python  
  
# install pip  
RUN curl -s https://bootstrap.pypa.io/get-pip.py > /tmp/get-pip.py  
RUN python /tmp/get-pip.py  
  
ENV GRAPHITE_VERSION 0.9.12  
# install graphite modules  
RUN apt-get update && apt-get install -y libcairo2-dev --fix-missing && rm -fr
/var/lib/apt/lists/*  
RUN pip install http://cairographics.org/releases/py2cairo-1.8.10.tar.gz  
  
RUN install -d -m 755 /var/lib/graphite  
WORKDIR /var/lib/graphite  
RUN pip install whisper==$GRAPHITE_VERSION \--install-option="--
prefix=/var/lib/graphite" \--install-option="--install-
lib=/var/lib/graphite/lib"  
RUN curl -sL https://raw.githubusercontent.com/graphite-
project/carbon/$GRAPHITE_VERSION/requirements.txt > /tmp/carbon-
requirements.txt  
RUN pip install -r /tmp/carbon-requirements.txt  
RUN pip install carbon==$GRAPHITE_VERSION \--install-option="--
prefix=/var/lib/graphite" \--install-option="--install-
lib=/var/lib/graphite/lib"  
RUN curl -sL https://raw.githubusercontent.com/graphite-project/graphite-
web/$GRAPHITE_VERSION/requirements.txt > /tmp/graphite-requirements.txt  
RUN pip install -r /tmp/graphite-requirements.txt  
RUN pip install uwsgi==2.0.1  
RUN pip install graphite-web==$GRAPHITE_VERSION \--install-option="--
prefix=/var/lib/graphite" \--install-option="--install-
lib=/var/lib/graphite/lib"  
  
RUN install -d m 755 /var/log/graphite  
RUN install -d -m 755 /etc/carbon  
COPY carbon /etc/carbon  
COPY graphite-web/local_settings.py
/var/lib/graphite/lib/graphite/local_settings.py  
COPY graphite-web/graphite.wsgi /var/lib/graphite/conf/graphite.wsgi  
COPY supervisord.conf /etc/supervisord.conf  
RUN touch /var/log/graphite/info.log /var/log/graphite/exception.log
/var/log/graphite/access.log /var/log/graphite/error.log  
  
ENV PYTHONPATH /var/lib/graphite/lib  
ENV LC_ALL en_US.UTF-8  
RUN python /var/lib/graphite/lib/graphite/manage.py syncdb --noinput  
  
EXPOSE 8000 2003 2004 7002  
VOLUME /var/log/graphite /var/lib/graphite/storage/whisper  
  
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisord.conf"]  

