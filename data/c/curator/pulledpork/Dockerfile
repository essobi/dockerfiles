FROM centos  
  
RUN /usr/bin/yum -y install tar perl-LWP-Protocol-https perl-Crypt-SSLeay
perl-Sys-Syslog perl-Archive-Tar perl-Mozilla-CA && yum clean all  
RUN /usr/bin/curl -O
"https://pulledpork.googlecode.com/files/pulledpork-0.7.0.tar.gz" &&
/usr/bin/tar xzvf pulledpork-0.7.0.tar.gz && /usr/bin/chmod +x
pulledpork-0.7.0/pulledpork.pl && /usr/bin/ln -s
/pulledpork-0.7.0/pulledpork.pl /usr/local/bin/pulledpork  
  
ENTRYPOINT ["/usr/local/bin/pulledpork"]  

