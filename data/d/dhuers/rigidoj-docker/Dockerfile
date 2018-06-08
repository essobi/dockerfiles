# VERSION 0.1.0  
  
FROM ubuntu:14.04  
  
MAINTAINER DHUers "https://github.com/DHUers"  
  
RUN echo "debconf debconf/frontend select Teletype" | debconf-set-selections
&&\  
echo "deb http://archive.ubuntu.com/ubuntu $(lsb_release -sc) main restricted
universe" > /etc/apt/sources.list &&\  
echo "deb http://archive.ubuntu.com/ubuntu $(lsb_release -sc)-updates main
restricted universe" >> /etc/apt/sources.list &&\  
echo "deb http://archive.ubuntu.com/ubuntu $(lsb_release -sc)-security main
restricted universe" >> /etc/apt/sources.list &&\  
apt-get update && apt-get -y install fping &&\  
sh -c "fping proxy && echo 'Acquire { Retries \"0\"; HTTP { Proxy
\"http://proxy:3128\";}; };' > /etc/apt/apt.conf.d/40proxy && apt-get update
|| true" &&\  
apt-get -y install software-properties-common &&\  
apt-get -y update &&\  
apt-mark hold initscripts &&\  
apt-get -y upgrade &&\  
add-apt-repository -y ppa:rwky/redis &&\  
add-apt-repository -y ppa:nginx/stable &&\  
add-apt-repository -y ppa:webupd8team/java &&\  
echo oracle-java7-installer shared/accepted-oracle-license-v1-1 select true |
/usr/bin/debconf-set-selections &&\  
apt-get install -y curl && curl
http://apt.postgresql.org/pub/repos/apt/ACCC4CF8.asc | apt-key add - &&\  
echo "deb http://apt.postgresql.org/pub/repos/apt/ trusty-pgdg main" | \  
tee /etc/apt/sources.list.d/postgres.list &&\  
curl https://www.rabbitmq.com/rabbitmq-signing-key-public.asc | apt-key add -
&&\  
echo "deb http://www.rabbitmq.com/debian/ testing main" | \  
tee /etc/apt/sources.list.d/rabbitmq.list &&\  
apt-get -y update &&\  
apt-get -y install build-essential git curl wget \  
libxslt-dev libcurl4-openssl-dev \  
libssl-dev libyaml-dev libtool \  
libxml2-dev gawk \  
pngcrush imagemagick gifsicle \  
postgresql-9.4 postgresql-client-9.4 \  
postgresql-contrib-9.4 libpq-dev libreadline-dev \  
nginx language-pack-en sudo cron anacron \  
psmisc rsyslog oracle-java7-installer rabbitmq-server clang &&\  
sed -i -e 's/start -q anacron/anacron -s/' /etc/cron.d/anacron &&\  
sed -i.bak 's/$ModLoad imklog/#$ModLoad imklog/' /etc/rsyslog.conf &&\  
dpkg-divert \--local --rename --add /sbin/initctl &&\  
sh -c "test -f /sbin/initctl || ln -s /bin/true /sbin/initctl" &&\  
apt-get -y install redis-server haproxy openssh-server &&\  
echo 'gem: --no-document' >> /usr/local/etc/gemrc &&\  
mkdir /src && cd /src && git clone https://github.com/sstephenson/ruby-
build.git &&\  
cd /src/ruby-build && ./install.sh &&\  
cd / && rm -rf /src/ruby-build &&\  
echo install_package "yaml-0.1.6"
"http://pyyaml.org/download/libyaml/yaml-0.1.6.tar.gz#5fe00cda18ca5daeb43762b80c38e06e"
\--if needs_yaml > /src/2.1.2.discourse &&\  
echo install_package "ruby-v_2_1_2_discourse"
"https://github.com/SamSaffron/ruby/archive/v_2_1_2_discourse.tar.gz#98741e3cbfd00ae2931b2c0edb0f0698"
ldflags_dirs standard verify_openssl >> /src/2.1.2.discourse &&\  
apt-get -y install ruby bison &&\  
ruby-build /src/2.1.2.discourse /usr/local &&\  
apt-get -y remove ruby1.9.1 &&\  
gem update --system &&\  
gem install bundler &&\  
cd / && git clone https://github.com/SamSaffron/pups.git &&\  
mkdir /jemalloc && cd /jemalloc &&\  
wget http://www.canonware.com/download/jemalloc/jemalloc-3.4.1.tar.bz2 &&\  
tar -xjf jemalloc-3.4.1.tar.bz2 && cd jemalloc-3.4.1 && ./configure && make
&&\  
mv lib/libjemalloc.so.1 /usr/lib && cd / && rm -rf /jemalloc &&\  
apt-get -y install runit monit socat &&\  
apt-get clean &&\  
rm -f /etc/apt/apt.conf.d/40proxy &&\  
locale-gen en_US.UTF-8 &&\  
mkdir -p /etc/runit/1.d &&\  
wget
https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-1.9.7-linux-x86_64.tar.bz2
&&\  
tar -xjf phantomjs-1.9.7-linux-x86_64.tar.bz2 &&\  
rm phantomjs-1.9.7-linux-x86_64.tar.bz2 &&\  
cp phantomjs-1.9.7-linux-x86_64/bin/phantomjs /bin/phantomjs &&\  
rm -fr phantomjs-1.9.7-linux-x86_64 &&\  
wget http://static.jonof.id.au/dl/kenutils/pngout-20130221-linux.tar.gz &&\  
tar -xf pngout-20130221-linux.tar.gz &&\  
rm pngout-20130221-linux.tar.gz &&\  
cp pngout-20130221-linux/x86_64/pngout /bin/pngout &&\  
rm -rf pngout-20130221-linux &&\  
useradd rigidoj -s /bin/bash -m -U &&\  
cd /var/www &&\  
git clone https://github.com/DHUers/rigidoj.git &&\  
chown -R rigidoj:rigidoj /var/www/rigidoj &&\  
cd /var/www/rigidoj &&\  
sudo -u rigidoj RAILS4=1 bundle install --deployment \  
\--without test --without development &&\  
cd /var/www/rigidoj/vendor/bundle &&\  
find . -name tmp -type d | xargs rm -rf && cd / &&\  
useradd rigidjudge -s /bin/bash -m -U &&\  
rm -fr /usr/share/man && rm -fr /usr/share/doc && mkdir -p /etc/runit/3.d #
clean up for docker squash  
  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8  
  
ADD runit-1 /etc/runit/1  
ADD runit-1.d-cleanup-pids /etc/runit/1.d/cleanup-pids  
ADD runit-1.d-anacron /etc/runit/1.d/anacron  
ADD runit-2 /etc/runit/2  
ADD runit-3 /etc/runit/3  
ADD boot /sbin/boot  
  
ADD cron /etc/service/cron/run  
ADD rsyslog /etc/service/rsyslog/run  
  
# this is temporary, remove in 2015  
RUN cp /sbin/boot /sbin/runit  

