# Description:  
#  
# To build aws nodejs lambdas you need a build environment  
# to package up the scripts in a zip file for uploading  
# to AWS. This image provides an AWS linux environment  
# for this task.  
#  
# Usage:  
# (Assumes the nodejs source and package.json is in the ./src folder and  
# the artifacts should go in the ./destination folder)  
# docker run --rm -ti -v $PWD/src:/src -v $PWD/src:/destination -w /src
dionjwa/aws-lambda-builder -s /src -d /destination  
#  
  
FROM amazonlinux:2016.09  
  
RUN mkdir /tmp/docker-build && \  
yum -y update && \  
curl -X GET -o /tmp/docker-build/RPM-GPG-KEY-lambda-epll https://lambda-
linux.io/RPM-GPG-KEY-lambda-epll && \  
rpm --import /tmp/docker-build/RPM-GPG-KEY-lambda-epll && \  
curl -X GET -o /tmp/docker-build/epll-release-2016.09-1.2.ll1.noarch.rpm
https://lambda-linux.io/epll-release-2016.09-1.2.ll1.noarch.rpm && \  
yum install -y /tmp/docker-build/epll-release-2016.09-1.2.ll1.noarch.rpm && \  
curl --silent --location https://rpm.nodesource.com/setup_6.x | bash - && \  
yum install -y nodejs && \  
yum install -y gcc gcc-c++ make && \  
yum install -y aws-cli && \  
yum install -y zip && \  
yum install -y jq && \  
yum clean all && \  
rm -rf /var/cache/yum/* && \  
rm -rf /tmp/* && \  
rm -rf /var/tmp/*  
  
ADD package-aws-lambda.sh /bin/package-aws-lambda.sh  
ENTRYPOINT ["/bin/bash", "/bin/package-aws-lambda.sh"]  

