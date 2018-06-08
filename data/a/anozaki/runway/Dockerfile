FROM docker:latest  
MAINTAINER "Akito Nozaki <anozaki@onica.com>"  
ENV TERRAFORM_VERSION=0.11.7  
ENV RUNWAY_VERSION=0.17.0  
RUN apk add --no-cache nodejs python python-dev py-pip build-base bash  
  
RUN npm i serverless -g \  
&& pip install stacker runway==${RUNWAY_VERSION} \--user \  
&& cd /tmp \  
&& wget
https://releases.hashicorp.com/terraform/${TERRAFORM_VERSION}/terraform_${TERRAFORM_VERSION}_linux_amd64.zip
\  
&& unzip terraform_${TERRAFORM_VERSION}_linux_amd64.zip \  
&& mv terraform /usr/local/bin \  
&& rm terraform_${TERRAFORM_VERSION}_linux_amd64.zip  
  
RUN rm -rf /root/.cache /root/.npm  
  
RUN mkdir /src  
ENV PATH=/root/.local/bin/:$PATH  
  
RUN apk update \  
&& apk add python3  
  
WORKDIR /src  

