FROM centos:7  
MAINTAINER heichblatt  
RUN /usr/bin/yum install -y https://fah.stanford.edu/file-
releases/public/release/fahclient/centos-5.3-64bit/v7.4/fahclient-7.4.4-1.x86_64.rpm
&& \  
/usr/bin/yum clean all  
VOLUME ["/var/lib/fahclient", "/etc/fahclient"]  
ENTRYPOINT ["/usr/bin/FAHClient", "--fold-anon"]  

