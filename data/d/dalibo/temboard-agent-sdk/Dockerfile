FROM centos:6  
  
RUN set -ex; \  
rpm --import \  
https://yum.postgresql.org/RPM-GPG-KEY-PGDG-10 \  
https://yum.postgresql.org/RPM-GPG-KEY-PGDG-94 \  
https://yum.postgresql.org/RPM-GPG-KEY-PGDG-95 \  
https://yum.postgresql.org/RPM-GPG-KEY-PGDG-96 \  
; \  
yum -q -y install \  
epel-release \  
https://download.postgresql.org/pub/repos/yum/9.4/redhat/rhel-6-x86_64/pgdg-
centos94-9.4-3.noarch.rpm \  
https://download.postgresql.org/pub/repos/yum/9.5/redhat/rhel-6-x86_64/pgdg-
centos95-9.5-3.noarch.rpm \  
https://download.postgresql.org/pub/repos/yum/9.6/redhat/rhel-6-x86_64/pgdg-
centos96-9.6-3.noarch.rpm \  
https://download.postgresql.org/pub/repos/yum/10/redhat/rhel-6-x86_64/pgdg-
centos10-10-2.noarch.rpm \  
; \  
yum -q -y install \  
postgresql94-server postgresql94-contrib \  
postgresql95-server postgresql95-contrib \  
postgresql96-server postgresql96-contrib \  
postgresql10-server postgresql10-contrib \  
; \  
yum clean all ; \  
:  
  
RUN set -ex; \  
yum -q -y install \  
http://opensource.wandisco.com/centos/6/git/x86_64/wandisco-git-
release-6-1.noarch.rpm \  
less \  
make \  
net-tools \  
openssl \  
procps-ng \  
psmisc \  
python-argparse \  
python-logutils \  
python-pip \  
rsync \  
sudo \  
; \  
yum clean all ; \  
:  
  
ADD https://github.com/krallin/tini/releases/download/v0.17.0/tini
/usr/local/sbin/tini  
  
RUN set -ex; \  
chmod +x /usr/local/sbin/tini; \  
pip install "pytest<3.3"; \  
rm -rf ~/.cache/; \  
useradd --system testuser; \  
:  
  
ENTRYPOINT ["/usr/local/sbin/tini", "-gw", "--"]  

