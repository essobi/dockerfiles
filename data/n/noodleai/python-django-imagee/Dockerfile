FROM python:3.5-slim  
  
MAINTAINER Gururaj Jeerge "gururaj@rangepro.in"  
EXPOSE 8000  
ENV HOME /root  
ENV APP_HOME /application/  
  
RUN apt-get update && \  
apt-get install -y --no-install-recommends build-essential \  
apt-transport-https \  
ca-certificates \  
gnupg \  
curl \  
git \  
imagemagick \  
libpq-dev \  
libxml2-dev \  
libxslt1-dev \  
openssh-client \  
file \  
libtiff5-dev \  
libjpeg-dev \  
zlib1g-dev \  
libfreetype6-dev \  
liblcms2-dev \  
tcl8.6-dev \  
tk8.6-dev \  
python-tk \  
graphviz \  
libgraphviz-dev \  
python-pydot \  
default-jre \  
default-jdk  
  
RUN curl -sL https://deb.nodesource.com/setup_6.x | bash -  
RUN apt-get install -y --no-install-recommends nodejs  
RUN ln -sf /usr/bin/nodejs /usr/local/bin/node  
RUN npm install -g phantomjs-prebuilt  
  
RUN curl -O https://bootstrap.pypa.io/get-pip.py  
RUN python get-pip.py  
RUN rm -f get-pip.py  
  
# Clean up APT and bundler when done.  
RUN rm -rf /usr/share/doc \  
/usr/share/man \  
/usr/share/groff \  
/usr/share/info \  
/usr/share/lintian \  
/usr/share/linda \  
/usr/share/locale/ \  
/var/cache/man  
  
# Clean up APT when done.  
RUN apt-get clean  
RUN apt-get autoclean  
RUN apt-get autoremove  
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Install bundle of gems  
RUN mkdir -p $APP_HOME  
WORKDIR $APP_HOME  
  
CMD ["tail", "-f", "/dev/null"]  

