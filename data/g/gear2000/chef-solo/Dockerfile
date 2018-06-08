FROM gear2000/ruby:16.04  
MAINTAINER Gary Leong <gwleong@gmail.com>  
  
RUN (apt-get -y update; \  
apt-get -y install python-software-properties curl build-essential libxml2-dev
libxslt-dev git ruby ruby-dev ca-certificates sudo net-tools vim; \  
apt-get -y dist-upgrade; \  
apt-get -y install locales; \  
echo "gem: --no-ri --no-rdoc" > ~/.gemrc; \  
gem install berkshelf; \  
apt-get autoremove -y; \  
apt-get clean -y; \  
rm -rf /var/cache/apt/archives/* /var/lib/apt/lists/*; \  
rm -rf /var/tmp/*)  
  
RUN (curl -L https://www.getchef.com/chef/install.sh | bash -s -- -v "12.3.0";
\  
apt-get autoremove -y; \  
apt-get clean -y; \  
rm -rf /var/cache/apt/archives/* /var/lib/apt/lists/*; \  
rm -rf /var/tmp/*)  
  
RUN echo 'en_US.UTF-8 UTF-8'>>/etc/locale.gen  
RUN locale-gen  
ENV LANG en_US.UTF-8  

