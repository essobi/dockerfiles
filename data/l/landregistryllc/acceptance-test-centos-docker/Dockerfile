FROM centos:7  
  
RUN curl --silent \--location https://rpm.nodesource.com/setup_4.x | bash - &&
\  
yum -y install nodejs && \  
npm install -g newman && \  
yum install -y centos-release-scl && \  
yum install -y rh-ruby22 rh-ruby22-rubygem-bundler rh-ruby22-ruby-devel && \  
yum install -y bzip2 && \  
echo "source /opt/rh/rh-ruby22/enable" > /etc/profile.d/ruby22.sh && \  
echo "export PATH=\$PATH:/opt/rh/rh-ruby22/root/usr/local/bin" >>
/etc/profile.d/ruby22.sh && \  
source /etc/profile.d/ruby22.sh && \  
mkdir -p /root/.phantomjs/2.1.1/x86_64-linux && \  
curl -SL
https://github.com/Medium/phantomjs/releases/download/v2.1.1/phantomjs-2.1.1-linux-x86_64.tar.bz2
| tar --strip 1 -xjC /root/.phantomjs/2.1.1/x86_64-linux && \  
yum groupinstall -y "Development Tools" && \  
yum install -y zlib-devel && \  
yum install -y zlib-devel freetype fontconfig && \  
yum clean all  

