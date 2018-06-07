FROM ergomentum/centos:7.2.160911182133  
MAINTAINER \  
Ergomentum <build@ergomentum.org>  
  
LABEL \  
vendor="Ergomentum" \  
license="Apache 2.0"  
  
ENV \  
GOPATH /root  
  
ENV \  
PATH="${PATH}:/usr/local/go/bin"  
RUN \  
# Workaround for https://bugzilla.redhat.com/show_bug.cgi?id=1213602  
touch /var/lib/rpm/* && \  
yum install git wget tar && \  
wget https://storage.googleapis.com/golang/go1.6.linux-amd64.tar.gz && \  
tar xzf go1.6.linux-amd64.tar.gz -C /usr/local && \  
rm go1.6.linux-amd64.tar.gz  
  
VOLUME \  
["/target"]  
  
COPY \  
common_functions.sh /  
COPY \  
entrypoint.sh /  
  
ENTRYPOINT \  
["/entrypoint.sh"]  

