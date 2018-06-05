FROM jenkinsci/jenkins  
  
# Switch from jenkins user to root to install packages  
USER root  
  
# Install docker debian-way  
RUN apt-get update && apt-get install apt-transport-https ca-certificates curl
gnupg2 software-properties-common -y --no-install-recommends && \  
curl -fsSL https://download.docker.com/linux/debian/gpg | apt-key add - && \  
add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/debian
$(lsb_release -cs) stable" && \  
apt-get update && apt-get install -y --no-install-recommends docker-ce  
  
# Install additional packages  
RUN apt-get update && apt-get install -y --no-install-recommends \  
autoconf \  
automake \  
bzip2 \  
cloc \  
default-libmysqlclient-dev \  
file \  
g++ \  
gcc \  
imagemagick \  
libbz2-dev \  
libc6-dev \  
libcurl4-openssl-dev \  
libdb-dev \  
libevent-dev \  
libffi-dev \  
libgeoip-dev \  
libglib2.0-dev \  
libjpeg-dev \  
liblzma-dev \  
libmagickcore-dev \  
libmagickwand-dev \  
libncurses-dev \  
libpng-dev \  
libpq-dev \  
libreadline-dev \  
libsqlite3-dev \  
libssl-dev \  
libtool \  
libwebp-dev \  
libxml2-dev \  
libxslt-dev \  
libyaml-dev \  
make \  
patch \  
python-dev \  
python-pip \  
python-setuptools \  
xz-utils \  
zlib1g-dev && \  
rm -rf /var/lib/apt/lists/* && \  
pip install -U docker-compose virtualenv envtpl  
  
# Allow jenkins to manage docker daemon  
# WARNING: This is high security risk as all jobs creators have now root
privilegues on HOST docker machine  
RUN groupadd -f docker && \  
usermod -aG docker jenkins && \  
usermod -aG www-data jenkins  
  
# Switch back to jenkins user  
USER jenkins  

