FROM ergomentum/centos:7.4.171101202856  
  
MAINTAINER \  
Ergomentum <build@ergomentum.org>  
  
LABEL \  
vendor="Ergomentum" \  
license="Apache 2.0"  
# Workaround for https://bugzilla.redhat.com/show_bug.cgi?id=1213602  
RUN \  
touch /var/lib/rpm/* && \  
yum install sudo rpm-build redhat-rpm-config shadow-utils && \  
yum groupinstall development && \  
yum clean all && \  
useradd -G wheel mockbuild && \  
sed \  
-E \  
-e 's/^%wheel.*$/%wheel\tALL=(ALL)\tNOPASSWD: ALL/' \  
-e 's/^Defaults.*requiretty$/#&/' \  
-i /etc/sudoers && \  
install -o mockbuild -g mockbuild -d
/home/mockbuild/rpmbuild/{BUILD,RPMS,SOURCES,SPECS,SRPMS} && \  
chown mockbuild:mockbuild /home/mockbuild/rpmbuild && \  
echo '%_topdir %(echo $HOME)/rpmbuild' > /home/mockbuild/.rpmmacros  
  
WORKDIR \  
/home/mockbuild  
  
USER \  
mockbuild  

