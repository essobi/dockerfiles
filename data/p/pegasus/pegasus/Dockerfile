FROM ubuntu:bionic  
  
LABEL maintainer="Rajiv Mayani <mayani@isi.edu>, Mats Rynge <rynge@isi.edu>"  
  
RUN apt-get update  
  
RUN useradd --gid 100 --uid 550 --create-home --password bamboo123 bamboo  
  
# Test requirements  
RUN apt-get -y install git ant ant-optional gcc g++ tar openjdk-8-jdk make
libmysql-java mpich bc python-setuptools python-dev libssl-dev libpq-dev
libmysqlclient-dev libffi-dev  
  
# Deb package build requirements  
RUN DEBIAN_FRONTEND=noninteractive apt-get -y install build-essential
debhelper asciidoc fop xsltproc lintian r-base libssl-dev python-openssl  
  
# Python requirements  
RUN apt-get -y install libsqlite3-dev && \  
easy_install pip && \  
pip install --upgrade pip setuptools && \  
pip install tox  
  
# Set Timezone  
RUN cp /usr/share/zoneinfo/America/Los_Angeles /etc/localtime  
  
USER bamboo  
  
RUN mkdir /home/bamboo/.pegasus  
  
ENV HOME /home/bamboo  
ENV PATH $HOME/.pyenv/bin:$PATH  
  
RUN curl -L https://raw.githubusercontent.com/pyenv/pyenv-
installer/master/bin/pyenv-installer | bash && \  
echo 'export PATH=~/.pyenv/bin:$PATH\neval "$(pyenv init -)"\neval "$(pyenv
virtualenv-init -)"' > ~/.bash_profile && \  
#pyenv install 2.6.9 && \  
pyenv install 2.7.14 && \  
#pyenv install 3.3.7 && \  
#pyenv install 3.4.8 && \  
pyenv install 3.5.5 && \  
pyenv install 3.6.4 && \  
pyenv global 2.7.14 3.5.5 3.6.4  
  
WORKDIR /home/bamboo/pegasus-source  

