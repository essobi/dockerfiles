FROM docker:stable-dind  
  
COPY config.json /root/.docker/config.json  
  
RUN apk add \--update \--no-cache ca-certificates openssl git make go gcc
libc-dev jq curl coreutils python3 \  
&& update-ca-certificates \  
&& go get -u github.com/awslabs/amazon-ecr-credential-helper/ecr-
login/cli/docker-credential-ecr-login \  
&& mv /root/go/bin/docker-credential-ecr-login /usr/local/bin/docker-
credential-ecr-login \  
&& mkdir -p /root/.docker \  
&& wget $(curl -Ls https://releases.hashicorp.com/index.json | jq
'{terraform}' | grep url | egrep linux_amd64 | sort -V | tail -n1 | awk
'{print $2}' | sed 's/"*,*//g') -O /tmp/terraform.zip \  
&& unzip /tmp/terraform.zip -d /usr/local/bin \  
&& curl -s https://bootstrap.pypa.io/get-pip.py -o get-pip.py \  
&& python3 get-pip.py \  
&& pip install awscli \  
&& pip3 install docker-compose \  
&& apk del make go gcc libc-dev jq curl coreutils \  
&& rm -rf /var/cache/apk/* \  
&& rm -Rf /root/go \  
&& rm -Rf /tmp/terraform.zip \  
&& aws \--version \  
&& terraform version \  
&& docker-compose \--version  

