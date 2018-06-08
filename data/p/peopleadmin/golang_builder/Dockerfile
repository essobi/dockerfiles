FROM golang:1.6-alpine  
  
RUN apk add --update \  
git \  
bash \  
curl \  
openssh-client \  
python python-dev \  
py-pip \  
&& pip install boto3==1.3.0 \  
&& rm -rf /var/cache/apk/*  
  
ADD
https://github.com/Masterminds/glide/releases/download/0.10.2/glide-0.10.2-linux-
amd64.tar.gz /root/  
RUN tar -C /root -xzf /root/glide-0.10.2-linux-amd64.tar.gz \  
&& cp /root/linux-amd64/glide /usr/local/bin/ \  
&& rm -rf /root/linux-amd64 glide-*  
  
RUN mkdir -p /root/.ssh \  
&& ssh-keyscan -t rsa bitbucket.org >> /root/.ssh/known_hosts \  
&& chmod 600 /root/.ssh/known_hosts  

