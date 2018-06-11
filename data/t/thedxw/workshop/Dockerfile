FROM ubuntu:17.10  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get update && \  
apt-get dist-upgrade -y && \  
rm -r /var/lib/apt/lists/*  
  
##############################################################################  
## Global configuration  
RUN apt-get update && \  
apt-get install --no-install-recommends -y locales tzdata sudo && \  
rm -r /var/lib/apt/lists/*  
  
# Fix "perl: warning: Setting locale failed."  
RUN locale-gen en_US.UTF-8 en_GB.UTF-8  
ENV LC_ALL=en_GB.UTF-8  
RUN echo Europe/London > /etc/timezone && \  
dpkg-reconfigure -f noninteractive tzdata  
# workaround: https://bugs.launchpad.net/ubuntu/+source/tzdata/+bug/1554806  
RUN ln -fs /usr/share/zoneinfo/Europe/London /etc/localtime  
  
RUN echo '%sudo ALL=(ALL:ALL) NOPASSWD: ALL' >> /etc/sudoers  
  
##############################################################################  
## Install tools  
RUN mkdir /src /home/core  
  
RUN apt-get update && \  
apt-get install --no-install-recommends -y \  
build-essential pkg-config automake software-properties-common apt-transport-
https \  
locales man-db manpages less manpages-dev \  
openssh-client tmux zsh vim-nox \  
git mercurial bzr tig git-flow \  
python3 python3-pip python3-setuptools python ruby ruby-dev perl perl-doc \  
php-cli php-gd php-mbstring php-mysql php-xml php-curl php-xdebug php-gmp \  
curl wget bind9-host netcat whois ca-certificates dnsutils net-tools \  
silversearcher-ag sloccount zip unzip \  
libpcre3-dev liblzma-dev libxml2-dev libxslt1-dev libmysql++-dev
libsqlite3-dev \  
optipng libtool nasm libjpeg-turbo-progs mysql-client nmap cloc ed ripmime
oathtool cloc \  
libcurl4-openssl-dev libexpat1-dev gettext asciidoc xsltproc xmlto iproute2
iputils-ping xmlstarlet gnupg2 tree jq libssl-dev && \  
rm -r /var/lib/apt/lists/*  
  
# Fix bad defaults  
RUN echo 'install: --no-rdoc --no-ri' > /etc/gemrc && \  
echo 'error_reporting=E_ALL' > /etc/php/7.1/cli/conf.d/99-dxw-errors.ini && \  
echo 'phar.readonly=Off' > /etc/php/7.1/cli/conf.d/99-dxw-phar.ini && \  
echo 'xdebug.var_display_max_depth=99999' > /etc/php/7.1/cli/conf.d/99-dxw-
fix-xdebug-var-dump.ini && \  
/bin/echo -e '[mail function]\nsendmail_path = /bin/false' >
/etc/php/7.1/cli/conf.d/99-dxw-disable-mail.ini && \  
echo '{"analytics":false}' > /home/core/.bowerrc  
  
# NodeJS  
RUN curl -s https://deb.nodesource.com/gpgkey/nodesource.gpg.key | apt-key add
- && \  
echo 'deb https://deb.nodesource.com/node_8.x '`lsb_release -c -s`' main' >
/etc/apt/sources.list.d/nodesource.list && \  
apt-get update && \  
apt-get install -y nodejs && \  
rm -r /var/lib/apt/lists/*  
  
# Update package managers  
RUN gem update --system  
  
# Go  
RUN wget --quiet https://storage.googleapis.com/golang/`curl -s
https://golang.org/VERSION?m=text`.linux-amd64.tar.gz -O /src/go.tar.gz && \  
tar -C /usr/local -xzf /src/go.tar.gz && \  
rm /src/go.tar.gz  
ENV PATH=$PATH:/usr/local/go/bin  
  
# Go tools  
RUN GOPATH=/src/go go get github.com/dxw/git-env && \  
GOPATH=/src/go go get github.com/holizz/pw && \  
GOPATH=/src/go go get github.com/holizz/diceware && \  
GOPATH=/src/go go get github.com/src-d/beanstool && \  
mv /src/go/bin/* /usr/local/bin/ && \  
rm -rf /src/go  
  
# composer  
RUN wget --quiet https://getcomposer.org/download/1.5.2/composer.phar -O
/usr/local/bin/composer && \  
chmod 755 /usr/local/bin/composer  
ENV PATH=$PATH:/usr/local/lib/composer/vendor/bin:~/.composer/vendor/bin  
  
# Heroku  
RUN echo "deb http://toolbelt.heroku.com/ubuntu ./" >
/etc/apt/sources.list.d/heroku.list && \  
wget --quiet -O- https://toolbelt.heroku.com/apt/release.key | apt-key add -
&& \  
apt-get update && \  
apt-get install -y heroku-toolbelt && \  
rm -r /var/lib/apt/lists/*  
  
# yarn  
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | sudo apt-key add - &&
\  
echo "deb https://dl.yarnpkg.com/debian/ stable main" >
/etc/apt/sources.list.d/yarn.list && \  
apt-get update && \  
apt-get install -y yarn && \  
rm -r /var/lib/apt/lists/*  
  
# Install things with package managers  
RUN gem install bundler sass && \  
pip3 install --upgrade docker-compose && \  
yarn global add grunt-cli bower json standard standard-format yo gulp  
  
# Other tools  
RUN git -C /src clone \--quiet --recursive https://github.com/dxw/srdb.git &&
\  
ln -s /src/srdb/srdb /usr/local/bin/srdb  
RUN git -C /src clone \--quiet --recursive https://github.com/dxw/whippet && \  
cp -r /src/whippet /usr/local/share/whippet && \  
ln -s /usr/local/share/whippet/bin/whippet /usr/local/bin/whippet  
RUN git -C /src clone \--quiet https://github.com/dxw/wpc && \  
cp /src/wpc/bin/* /usr/local/bin  
  
##############################################################################  
## Add user  
RUN adduser --gecos '' \--shell /bin/zsh --disabled-password core  
RUN usermod -aG sudo core  
  
##############################################################################  
## Startup  
WORKDIR /workbench  
USER core  
VOLUME /workbench  
CMD ["tmux", "-u2"]  

