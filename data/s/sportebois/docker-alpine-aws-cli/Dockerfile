# Alpine 3.6 is current latest  
FROM alpine:3.6  
ENV AWS_CLI_VERSION=1.14.35  
RUN apk --update --no-cache add \  
python \  
py-pip \  
jq \  
bash \  
git \  
&& pip install --no-cache-dir awscli==$AWS_CLI_VERSION \  
&& apk del py-pip \  
&& rm -rf /var/cache/apk/* /root/.cache/pip/* /usr/lib/python2.7/site-
packages/awscli/examples  
  
# Expose .aws to mount config/credentials  
VOLUME /root/.aws  
  
# Expose workspace to mount stuff  
VOLUME /workspace  
WORKDIR /workspace  
  
ENTRYPOINT [ "aws" ]  

