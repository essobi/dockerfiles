FROM alpine:3.4  
ENV TERRAFORM_VERSION 0.9.4  
RUN mkdir /root/.aws  
  
RUN apk update && \  
apk add python py-pip make openssh && \  
apk add --update wget ca-certificates unzip git bash groff less jq && \  
pip install --upgrade awscli && \  
wget -q -O /terraform.zip
"https://releases.hashicorp.com/terraform/${TERRAFORM_VERSION}/terraform_${TERRAFORM_VERSION}_linux_amd64.zip"
&& \  
unzip /terraform.zip -d /bin && \  
apk del --purge wget ca-certificates unzip && \  
apk del py-pip && \  
apk del py-setuptools && \  
rm -rf /var/cache/apk/* /terraform.zip && \  
rm -rf /tmp/*  
  
VOLUME ["/data"]  
WORKDIR /data  
  
ENTRYPOINT ["/srv/dispatch"]  
  
ADD ./dispatch /srv/dispatch  

