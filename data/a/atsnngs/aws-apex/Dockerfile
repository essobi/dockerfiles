FROM mhart/alpine-node:4.3  
RUN apk add --update jq curl python py-pip make bash \  
libc6-compat python-dev gcc musl-dev libffi-dev openssl-dev git  
RUN curl https://raw.githubusercontent.com/apex/apex/master/install.sh | sh &&
apex upgrade  
RUN pip install --upgrade pip  
RUN pip install awscli  
RUN pip install awscurl  
  
ENV TERRAFORM_VERSION 0.11.7  
RUN cd /usr/bin && \  
curl
https://releases.hashicorp.com/terraform/${TERRAFORM_VERSION}/terraform_${TERRAFORM_VERSION}_linux_amd64.zip
-o terraform_${TERRAFORM_VERSION}_linux_amd64.zip && \  
unzip terraform_${TERRAFORM_VERSION}_linux_amd64.zip && \  
rm terraform_${TERRAFORM_VERSION}_linux_amd64.zip  

