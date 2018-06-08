FROM centos:centos7  
MAINTAINER Marcin Ryzycki marcin@m12.io, Przemyslaw Ozgo linux@ozgo.info  
  
RUN \  
yum update -y && \  
yum install -y git perl-App-cpanminus tar gzip zip gcc make && \  
curl https://raw.githubusercontent.com/timkay/aws/master/aws -o
/usr/local/src/aws && \  
chmod +x /usr/local/src/aws && \  
/usr/local/src/aws --install && \  
yum remove -y gcc make && \  
yum clean all  
  
COPY bootstrap.sh /  
  
ENV EC2_ACCESS_KEY=key EC2_SECRET_KEY=key  
  
ENTRYPOINT ["/bootstrap.sh"]

