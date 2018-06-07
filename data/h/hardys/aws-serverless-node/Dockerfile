FROM node:6.10-alpine  
MAINTAINER Hardys <hardyscc@gmail.com>  
  
RUN apk add --no-cache \  
python \  
py-pip \  
ca-certificates \  
groff \  
less \  
bash \  
&& pip install --no-cache-dir --upgrade pip awscli  
  
RUN npm -g install serverless@1.23.0  
  
WORKDIR /root  
CMD bash  

