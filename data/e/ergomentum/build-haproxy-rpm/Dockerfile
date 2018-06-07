FROM ergomentum/rpmbuild:7.2.160911200336  
MAINTAINER \  
Ergomentum <build@ergomentum.org>  
  
LABEL \  
vendor="Ergomentum" \  
license="Apache 2.0"  
  
RUN \  
# Workaround for https://bugzilla.redhat.com/show_bug.cgi?id=1213602  
sudo touch /var/lib/rpm/* && \  
sudo yum install pcre-devel zlib-devel openssl-devel systemd-units && \  
sudo yum clean all && \  
sudo localedef --force --inputfile=en_US --charmap=ISO-8859-1 en_US.ISO-8859-1  
VOLUME \  
["/target"]  
  
COPY \  
common_functions.sh /home/mockbuild  
COPY \  
entrypoint.sh /home/mockbuild  
COPY \  
log.patch /home/mockbuild/rpmbuild/SOURCES  
  
ENTRYPOINT \  
["./entrypoint.sh"]  

