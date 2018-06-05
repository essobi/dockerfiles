FROM miko2u/centos6  
MAINTAINER miko@cafelounge.net  
  
# packages  
RUN cd /tmp \  
&& printf "[cafelounge]\n\  
name=cafelounge repository for CentOS \$releasever - \$basearch\n\  
baseurl=http://repo.cafelounge.net/yum/el/\$releasever/\$basearch/\n\  
gpgcheck=1\n\  
enabled=0\n\  
gpgkey=http://repo.cafelounge.net/yum/el/\$releasever/RPM-GPG-KEY-
cafelounge\n\  
" > /etc/yum.repos.d/cafelounge.repo \  
&& yum -y update \  
&& curl -OL
http://repo.cafelounge.net/yum/el/6/x86_64/ruby-2.1.6-2.el6.x86_64.rpm \  
&& yum -y localinstall ruby-2.1.6-2.el6.x86_64.rpm \  
&& rm -rf /tmp/*.rpm \  
&& echo "install: --no-document" > /root/.gemrc \  
&& echo "update: --no-document" >> /root/.gemrc \  
&& gem install bundler  

