FROM concourse/buildroot:git  
  
MAINTAINER Caleb Washburn "cwashburn@pivotal.io"  
  
ADD https://github.com/pivotalservices/cf-mgmt/releases/download/v0.0.61/cf-
mgmt-linux /usr/bin/cf-mgmt  
RUN chmod +x /usr/bin/cf-mgmt && cf-mgmt --version  

