FROM tico/docker  
MAINTAINER Dabija Afanasie <faneldabija2008@gmail.com>  
  
ENV TERRAFORM_VERSION 0.11.7  
ADD
"https://releases.hashicorp.com/terraform/${TERRAFORM_VERSION}/terraform_${TERRAFORM_VERSION}_linux_amd64.zip"
/tmp/terraform.zip  
  
RUN apk --no-cache add nodejs nodejs-npm && \  
unzip /tmp/terraform.zip -d /tmp && mv /tmp/terraform /usr/local/bin/terraform  
  
RUN mkdir -p /opt/citf  
  
COPY citf/* /opt/citf/  
COPY bin.sh /usr/local/bin/citf  
  
RUN chmod +x /usr/local/bin/*  
RUN npm install -g tf-output  
  

