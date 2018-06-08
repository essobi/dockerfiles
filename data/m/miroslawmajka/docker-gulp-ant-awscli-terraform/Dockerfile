# Use a minimal Linux container with Node.js version 6.x.x  
FROM mhart/alpine-node:6  
# Install Gulp via npm  
RUN npm install -g gulp  
  
# Run Alpine package update  
RUN apk update  
  
# Install Ant  
RUN apk add apache-ant ca-certificates unzip openssl  
  
# Install Python and PIP  
RUN apk add python  
RUN apk add py-pip  
  
# Install AWS CLI via PIP  
RUN pip install awscli  
  
# Terraform  
ENV TERRAFORM_VERSION=0.9.11  
RUN wget
https://releases.hashicorp.com/terraform/$TERRAFORM_VERSION/terraform_${TERRAFORM_VERSION}_linux_amd64.zip
&& \  
unzip terraform_${TERRAFORM_VERSION}_linux_amd64.zip && rm
terraform_${TERRAFORM_VERSION}_linux_amd64.zip && \  
mv terraform /usr/bin/  
  
ENTRYPOINT ["/bin/sh", "-c"]  

