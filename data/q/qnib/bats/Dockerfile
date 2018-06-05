FROM qnib/supervisor  
  
RUN yum install -y bsdtar  
RUN curl -fsL https://github.com/sstephenson/bats/archive/master.zip |bsdtar
xf - -C /opt/ && \  
cp /opt/bats-master/libexec/bats* /usr/local/libexec/ && \  
chmod +x /usr/local/libexec/bats* && \  
rm -rf /opt/bats-master/  

