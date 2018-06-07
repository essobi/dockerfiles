FROM ubuntu:14.04  
MAINTAINER Lewis  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN \  
echo 'APT::Get::Assume-Yes "true";' > /etc/apt/apt.conf.d/90forceyes ;\  
echo 'deb http://archive.ubuntu.com/ubuntu trusty main universe restricted' >
/etc/apt/sources.list ;\  
echo 'deb http://archive.ubuntu.com/ubuntu trusty-updates main universe
restricted' >> /etc/apt/sources.list ;\  
apt-get update ;\  
echo exit 101 > /usr/sbin/policy-rc.d && chmod +x /usr/sbin/policy-rc.d ;\  
dpkg-divert --local \--rename --add /sbin/initctl ;\  
ln -sf /bin/true /sbin/initctl ;\  
apt-get -y upgrade ;\  
apt-get install -y tar python-software-properties build-essential curl
libreadline-dev libcurl4-gnutls-dev libpq-dev libxml2-dev libxslt1-dev
zlib1g-dev libssl-dev git-core libmagickwand-dev ;\  
apt-get clean  
  
RUN curl https://s3.amazonaws.com/pkgr-buildpack-
ruby/current/ubuntu-14.04/ruby-2.1.4.tgz -o - | tar xzf - -C /usr/local  
  
RUN \  
cd /opt ;\  
git clone https://github.com/feedbin/feedbin.git ;\  
cd feedbin ;\  
gem install bundler redis ;\  
bundle install ;\  
bundle  
  
RUN apt-get install -y postgresql  
  
ADD config/database.yml /opt/feedbin/config/database.yml  
  
ADD subscriptions_controller.rb
/opt/feedbin/app/controllers/subscriptions_controller.rb  
  
ADD startup.sh /feedbin-start  
  
CMD ["/bin/bash", "/feedbin-start"]  
  
EXPOSE 9292  

