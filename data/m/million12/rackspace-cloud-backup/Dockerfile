#  
# million12/rackspace-cloud-backup  
#  
FROM centos:centos7  
MAINTAINER Marcin Ryzycki marcin@m12.io  
  
RUN \  
curl -sSL -o /etc/yum.repos.d/drivesrvr.repo
http://agentrepo.drivesrvr.com/redhat/drivesrvr.repo && \  
yum update -y && \  
yum install -y ca-certificates tar driveclient && \  
yum clean all && \  
  
mkdir /etc/driveclient && \  
ln -s /etc/pki/ca-trust/extracted/pem/tls-ca-bundle.pem
/etc/driveclient/cacert.pem  
  
COPY container-files /  
RUN chmod +x /run.sh  
  
ENV API_HOST lon.backup.api.rackspacecloud.com  
ENV API_KEY 32lengthApiKeyFromYourRaxAccount  
ENV ACCOUNT_ID 01234567  
ENV USERNAME account-username  
  
CMD ["/run.sh"]  

