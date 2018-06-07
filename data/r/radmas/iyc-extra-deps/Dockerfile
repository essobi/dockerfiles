FROM radmas/iyc-basic-deps-php  
  
MAINTAINER fernando.moro@radmas.com  
  
ENV DEBIAN_FRONTEND noninteractive  
  
#################################################  
# WKHTMLTOPDF  
  
ENV WKHTMLTOPDF_FILENAME wkhtmltox-0.12.3_linux-generic-amd64.tar.xz  
ENV WKHTMLTOPDF_LINK
http://download.gna.org/wkhtmltopdf/0.12/0.12.3/wkhtmltox-0.12.3_linux-
generic-amd64.tar.xz  
  
RUN \  
cd /opt && \  
wget ${WKHTMLTOPDF_LINK} && \  
tar -xJf ${WKHTMLTOPDF_FILENAME} && \  
rm -f ${WKHTMLTOPDF_FILENAME}  
  
RUN ln -s /opt/wkhtmltox/bin/wkhtmltopdf /usr/bin/.  
  
# install WKHTMLTOPDF dependencies  
RUN \  
apt-get update && \  
apt-get -y upgrade && \  
apt-get install -y \  
fontconfig \  
libfontconfig1 \  
libfreetype6 \  
libpng12-0 \  
zlib1g \  
libjpeg-turbo8 \  
libssl1.0.0 \  
libx11-6 \  
libxext6 \  
libxrender1 \  
libstdc++6 \  
libc6 && \  
rm -rf /var/lib/apt/lists/*  
#################################################  
# AWS cli  
  
RUN \  
apt-get update && \  
apt-get -y upgrade && \  
apt-get install -y \  
awscli && \  
rm -rf /var/lib/apt/lists/*  
#################################################  
# JAVA 7  
  
RUN \  
echo oracle-java7-installer shared/accepted-oracle-license-v1-1 select true |
debconf-set-selections && \  
add-apt-repository -y ppa:webupd8team/java && \  
apt-get update && \  
apt-get install -y \  
oracle-java7-installer && \  
rm -rf /var/cache/oracle-jdk7-installer && \  
rm -rf /var/lib/apt/lists/*  
# define JAVA_HOME variable  
ENV JAVA_HOME=/usr/lib/jvm/java-7-oracle  
  
#################################################  
# PYTHON  
  
RUN \  
apt-get update && \  
apt-get -y upgrade && \  
apt-get install -y \  
python \  
python-dev \  
python-pip \  
python-virtualenv && \  
rm -rf /var/lib/apt/lists/*  
#################################################  
# NODE.JS  
  
ENV NODE_VERSION v0.10.36  
  
RUN \  
cd /tmp && \  
wget
http://nodejs.org/dist/${NODE_VERSION}/node-${NODE_VERSION}-linux-x64.tar.gz
&& \  
tar -C /usr/local --strip-components 1 -xzf
node-${NODE_VERSION}-linux-x64.tar.gz && \  
cd /tmp && \  
rm -rf /tmp/node-v* && \  
npm install -g npm  
  
# define node.js variables  
ENV PATH node_modules/.bin:$PATH  
ENV NODE_PATH /usr/local/lib/node_modules  
# install node.js dependencies  
RUN \  
npm install -g \  
bower \  
grunt-cli \  
coffee-script \  
less@1.7.5  
# NPM FIX (Prevent docker EXDEV error )  
RUN \  
cd $(npm root -g)/npm && \  
npm install fs-extra && \  
sed -i -e s/graceful-fs/fs-extra/ -e s/fs.rename/fs.move/
./lib/utils/rename.js  
#################################################  
# RUBY  
  
ENV RUBY_VERSION 2.2  
# install ruby from PPA  
RUN \  
add-apt-repository -y ppa:brightbox/ruby-ng && \  
apt-get update && \  
apt-get install -y \  
ruby${RUBY_VERSION} \  
ruby${RUBY_VERSION}-dev \  
ruby-switch && \  
rm -rf /var/lib/apt/lists/*  
# switch default ruby version  
RUN \  
ruby-switch --set ruby${RUBY_VERSION}  
  
# install ruby gems  
RUN \  
gem install \  
premailer \  
nokogiri  
  
#################################################  
# SUPERVISOR  
  
RUN \  
apt-get update && \  
apt-get -y upgrade && \  
apt-get install -y \  
supervisor && \  
rm -rf /var/lib/apt/lists/*  
  
RUN mkdir -p /var/log/supervisor  
  
#################################################  
  
CMD ["/usr/bin/supervisord"]  

