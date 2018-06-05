FROM centos:7  
  
MAINTAINER Sebastien LANGOUREAUX <sebastien.langoureaux@sihm.fr>  
  
ARG http_proxy  
ARG https_proxy  
  
ENV AMBARI_URL="http://public-
repo-1.hortonworks.com/ambari/centos7/2.x/updates/2.6.1.3/ambari.repo" \  
HDP_URL="http://public-
repo-1.hortonworks.com/HDP/centos7/2.x/updates/2.6.4.0/hdp.repo" \  
HDP_GPL_URL="http://public-repo-1.hortonworks.com/HDP-
GPL/centos7/2.x/updates/2.6.4.0/hdp.gpl.repo" \  
HDP_SEARCH_URL="http://public-repo-1.hortonworks.com/HDP-
SOLR-2.6-100/repos/centos7/hdp-solr.repo" \  
AMBARI_VERSION="2.6.1.3" \  
HDP_VERSION="2.6.4.0" \  
HDP_UTILS_VERSION="1.1.0.22" \  
HDP_GPL_VERSION="2.6.4.0" \  
HDP_SEARCH_VERSION="2.6-100"  
  
  
RUN \  
sed -i 's/enabled=1/enabled=0/g' /etc/yum/pluginconf.d/fastestmirror.conf &&\  
yum install -y createrepo yum-utils httpd curl &&\  
curl -Lo /etc/yum.repos.d/ambari.repo ${AMBARI_URL} &&\  
curl -Lo /etc/yum.repos.d/hdp.repo ${HDP_URL} &&\  
curl -Lo /etc/yum.repos.d/hdp-gpl.repo ${HDP_GPL_URL} &&\  
curl -Lo /etc/yum.repos.d/hdp-search.repo ${HDP_SEARCH_URL} &&\  
cd /var/www/html/ &&\  
mkdir -p ambari/centos7 &&\  
cd ambari/centos7/ &&\  
reposync -r ambari-${AMBARI_VERSION} &&\  
createrepo ambari-${AMBARI_VERSION} &&\  
cd /var/www/html/ &&\  
mkdir -p hdp/centos7 &&\  
cd hdp/centos7/ &&\  
reposync -r HDP-${HDP_VERSION} &&\  
createrepo HDP-${HDP_VERSION} &&\  
cd /var/www/html/ &&\  
mkdir -p hdp-utils/centos7 &&\  
cd hdp-utils/centos7/ &&\  
reposync -r HDP-UTILS-${HDP_UTILS_VERSION} &&\  
createrepo HDP-UTILS-${HDP_UTILS_VERSION} &&\  
cd /var/www/html/ &&\  
mkdir -p hdp-gpl/centos7 &&\  
cd hdp-gpl/centos7/ &&\  
reposync -r HDP-GPL-${HDP_GPL_VERSION} &&\  
createrepo HDP-GPL-${HDP_GPL_VERSION} &&\  
cd /var/www/html/ &&\  
mkdir -p hdp-search/centos7 &&\  
cd hdp-search/centos7/ &&\  
reposync -r HDP-SOLR-${HDP_SEARCH_VERSION} &&\  
createrepo HDP-SOLR-${HDP_SEARCH_VERSION} &&\  
yum clean packages  
  
# Systemd  
RUN (cd /lib/systemd/system/sysinit.target.wants/; for i in *; do [ $i ==
systemd-tmpfiles-setup.service ] || rm -f $i; done); \  
rm -f /lib/systemd/system/multi-user.target.wants/*;\  
rm -f /etc/systemd/system/*.wants/*;\  
rm -f /lib/systemd/system/local-fs.target.wants/*; \  
rm -f /lib/systemd/system/sockets.target.wants/*udev*; \  
rm -f /lib/systemd/system/sockets.target.wants/*initctl*; \  
rm -f /lib/systemd/system/basic.target.wants/*;\  
rm -f /lib/systemd/system/anaconda.target.wants/*;  
  
RUN systemctl enable httpd  
  
  
VOLUME [ "/sys/fs/cgroup" ]  
  
CMD ["/usr/sbin/init"]

