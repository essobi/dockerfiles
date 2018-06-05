FROM amazonlinux:1  
RUN curl -sL https://github.com/bats-core/bats-core/archive/v0.4.0.tar.gz |
tar zx -C /opt \  
&& ln -s /opt/bats-core-0.4.0/libexec/bats /usr/local/bin  
  
ENTRYPOINT ["bats"]  

