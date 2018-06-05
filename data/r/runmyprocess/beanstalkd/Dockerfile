FROM fedora:latest  
RUN dnf install -y beanstalkd && dnf clean all  
RUN mkdir -p /data/beanstalkd/  
EXPOSE 11300  
ENTRYPOINT /usr/bin/beanstalkd -l 0.0.0.0 -p 11300 -z 65535 -b
/data/beanstalkd/ -f 500 -s 10485760  

