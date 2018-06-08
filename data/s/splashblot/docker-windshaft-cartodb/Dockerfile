#  
# Windshaft-cartodb container  
#  
FROM ubuntu:14.04  
MAINTAINER Juanjo Mata <jjmata@tileo.co>  
  
# Configuring locales  
ENV DEBIAN_FRONTEND noninteractive  
RUN dpkg-reconfigure locales && \  
locale-gen en_US.UTF-8 && \  
update-locale LANG=en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8  
ENV ENVIRONMENT development  
  
RUN apt-get update && apt-get install -y -q curl software-properties-common  
RUN curl -sL https://deb.nodesource.com/setup_6.x | sudo -E bash -  
  
RUN curl -sL https://www.postgresql.org/media/keys/ACCC4CF8.asc | \  
apt-key add -  
RUN sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt/ trusty-pgdg
main" >> /etc/apt/sources.list.d/postgresql.list'  
  
RUN add-apt-repository ppa:ubuntu-toolchain-r/test  
RUN apt-get update && \  
apt-get install -y -q \  
make g++-4.9 pkg-config git-core \  
libgif-dev libjpeg8-dev libcairo2-dev libpango1.0-dev \  
libhiredis-dev redis-server \  
nodejs \  
postgresql-9.5-postgis-2.3 postgresql-plpython-9.5  
  
RUN curl -sS http://dl.yarnpkg.com/debian/pubkey.gpg | sudo apt-key add -  
RUN echo "deb http://dl.yarnpkg.com/debian/ stable main" | sudo tee
/etc/apt/sources.list.d/yarn.list  
RUN apt-get update && apt-get install -y -q yarn  
  
# Install Windshaft  
RUN git clone git://github.com/CartoDB/Windshaft-cartodb.git && \  
cd Windshaft-cartodb && yarn && mkdir logs  
  
# Expose Windshaft port  
EXPOSE 8181  
CMD cd /CartoDB-SQL-API; node app.js $ENVIRONMENT

