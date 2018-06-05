#  
# Dockerfile - Spacewalk  
#  
# - Build  
# hg clone https://bitbucket.org/bashell-com/spacewalk /opt/docker-spacewalk  
# docker build --rm -t spacewalk /opt/docker-spacewalk  
#  
# - Run  
# docker run --privileged=true -d --name="spacewalk" -h "spackewalk" spacewalk  
# 1. Base images  
FROM centos:6  
MAINTAINER Chaiwat Suttipongsakul <cwt@bashell.com>  
  
# 2. Set the environment variable  
WORKDIR /opt  
ENV VERSION=2.6  
ENV RELEASE=0  
# 3. Add the epel, spacewalk, jpackage, supervisord  
ADD conf/jpackage.repo /etc/yum.repos.d/jpackage.repo  
RUN yum install -y epel-release \  
&& yum install -y
http://yum.spacewalkproject.org/$VERSION/RHEL/6/x86_64/spacewalk-
repo-$VERSION-$RELEASE.el6.noarch.rpm \  
&& yum check-update ; yum upgrade -y \  
&& yum install -y spacewalk-setup-postgresql spacewalk-postgresql tomcat-
native python-setuptools python-pip \  
&& yum clean all \  
&& pip install supervisor && pip install --upgrade meld3==0.6.10 && mkdir
/etc/supervisord.d \  
&& rm -rf /root/.cache  
  
# 4. Install supervisord config  
ADD conf/supervisord.conf /etc/supervisord.d/supervisord.conf  
  
# 5. Install spacewalk initial and running scripts  
ADD conf/answer.txt /opt/answer.txt  
ADD conf/spacewalk.sh /opt/spacewalk.sh  
  
# 6. Start supervisord  
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisord.d/supervisord.conf"]  
  
# System Log  
VOLUME /var/log  
  
# PostgreSQL Data  
VOLUME /var/lib/pgsql/data  
  
# RPM repository  
VOLUME /var/satellite  
  
# Bootstrap directory  
VOLUME /var/www/html/pub  
  
# Port  
EXPOSE 80 443  

