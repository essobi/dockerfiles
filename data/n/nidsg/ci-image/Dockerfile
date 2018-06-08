FROM docker:stable-git  
  
ENV TERRAFORM_VERSION=0.11.7  
  
RUN apk --no-cache add --update \  
bash \  
ca-certificates \  
curl \  
jq \  
make \  
perl \  
py-pip \  
tar \  
unzip && \  
rm -rf /var/cache/apk/*  
  
RUN pip --no-cache-dir install \  
awscli \  
boto3 \  
docker-compose \  
ecs-deploy  
  
RUN cd /tmp && \  
curl -o terraform.zip
https://releases.hashicorp.com/terraform/${TERRAFORM_VERSION}/terraform_${TERRAFORM_VERSION}_linux_amd64.zip
&& \  
unzip terraform.zip -d /usr/bin && \  
rm -rf /tmp/*  

