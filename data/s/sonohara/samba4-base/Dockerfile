FROM sonohara/centos7-base:latest  
MAINTAINER Expert Software Inc. / https://www.e-software.company  
  
LABEL name="Samba 4" \  
vendor="ExpertSoftware Inc." \  
license="GPLv3" \  
build-date="20171119" \  
build-tag="1.0.0_3" \  
build-version="3"  
RUN yum install -y authconfig krb5-workstation || true  
  
RUN wget http://wing-net.ddo.jp/wing/7/EL7.wing.repo \  
&& sed -i 's@enabled=0@enabled=1@g' EL7.wing.repo \  
&& mv EL7.wing.repo /etc/yum.repos.d/  
  
RUN yum install -y samba46 \  
samba46-winbind-clients samba46-winbind \  
samba46-client samba46-common-tools samba46-dc samba46-pidl samba46-python \  
samba46-winbind-krb5-locator perl-Parse-Yapp python2-crypto || true  
  
RUN yum clean all | true  
  
VOLUME ["/var/lib/samba", "/var/log/samba", "/etc/samba", "/.docker"]  

