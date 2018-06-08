FROM jenkins  
  
USER root  
  
# This is necessary to get the latest ver of Node.js mainly  
# because javascript is really silly  
RUN curl -sL https://deb.nodesource.com/setup_0.12 | bash -  
  
# Install additional tools / package dependencies for building stuff  
RUN apt-get update && apt-get install -qqy \  
make \  
automake \  
gcc \  
autoconf \  
bison \  
build-essential \  
bzip2 \  
libssl-dev \  
libyaml-dev \  
libreadline6-dev \  
zlib1g-dev \  
libncurses5-dev \  
libffi-dev \  
libgdbm3 \  
libgdbm-dev \  
libpq-dev \  
python-setuptools \  
python-dev \  
python-pip \  
nodejs \  
xvfb  
  
# Install firefox for selenium UI tests  
RUN wget -q
https://ftp.mozilla.org/pub/mozilla.org/firefox/releases/41.0/linux-x86_64/en-
US/firefox-41.0.tar.bz2 && \  
tar xvjf firefox-41.0.tar.bz2 -C /opt && \  
ln -s /opt/firefox/firefox /usr/bin/firefox && \  
rm firefox-41.0.tar.bz2  
  
# Install frontend build tools  
RUN npm install -g gulp  
  
# Install ansible using pip  
RUN pip install ansible -q  
  
# Install tutum cli using pip  
RUN pip install tutum -q  
  
# Add jenkins as a docker user  
RUN groupadd -g 999 docker  
RUN gpasswd -a jenkins docker  
  
USER jenkins  

