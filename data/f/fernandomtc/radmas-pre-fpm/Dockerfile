FROM ubuntu:14.04  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update && apt-get install -y \  
php5-cli \  
php5-fpm \  
curl \  
php5-curl \  
php5-json \  
php5-mongo \  
php5-redis \  
php5-gd \  
php5-intl \  
php-apc \  
gearman-job-server \  
php5-gearman \  
php-pear \  
zlib1g-dev \  
wget \  
fontconfig \  
libxrender1 \  
libxext6  
  
# install HTMLtoPDF  
ADD wkhtmltox-0.12.1-trusty-amd64.deb /wkhtmltox-0.12.1-trusty-amd64.deb  
RUN dpkg -i /wkhtmltox-0.12.1-trusty-amd64.deb  
RUN ln -s /usr/local/bin/wkhtmltopdf /usr/bin/.  
  
# install build tools  
RUN \  
sed -i 's/# \\(.*multiverse$\\)/\1/g' /etc/apt/sources.list && \  
apt-get update && \  
apt-get -y upgrade && \  
apt-get install -y build-essential && \  
apt-get install -y software-properties-common && \  
apt-get install -y byobu curl git htop man unzip vim wget  
  
# install aws  
RUN apt-get update && apt-get install -y awscli  
  
# install Java  
RUN \  
echo oracle-java7-installer shared/accepted-oracle-license-v1-1 select true |
debconf-set-selections && \  
add-apt-repository -y ppa:webupd8team/java && \  
apt-get update && \  
apt-get install -y oracle-java7-installer && \  
rm -rf /var/lib/apt/lists/* && \  
rm -rf /var/cache/oracle-jdk7-installer  
  
# define commonly used JAVA_HOME variable  
ENV JAVA_HOME /usr/lib/jvm/java-7-oracle  
  
# install Ruby  
RUN \  
apt-get update && \  
apt-get install -y ruby1.9.3 && \  
rm -rf /var/lib/apt/lists/*  
  
RUN gem install premailer nokogiri  
  
# install nodejs  
RUN \  
cd /tmp && \  
wget http://nodejs.org/dist/v0.10.36/node-v0.10.36-linux-x64.tar.gz && \  
tar -C /usr/local \--strip-components 1 -xzf node-v0.10.36-linux-x64.tar.gz &&
\  
cd /tmp && \  
rm -rf /tmp/node-v* && \  
npm install -g npm  
  
ENV PATH node_modules/.bin:$PATH  
ENV NODE_PATH /usr/local/lib/node_modules  
  
RUN npm install -g coffee-script  
  
# install supervisor daemon  
RUN apt-get update && apt-get install -y supervisor  
RUN mkdir -p /var/log/supervisor  
  
# run daemon  
CMD ["/usr/bin/supervisord"]  

