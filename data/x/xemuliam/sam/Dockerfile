FROM xemuliam/alpine:3.7  
MAINTAINER Viacheslav Kalashnikov <xemuliam@gmail.com>  
ARG DIST_MIRROR=https://github.com/awslabs/aws-sam-local/releases  
ENV VERSION=0.2.6 \  
SAM_HOME=/opt/sam  
RUN mkdir -p ${SAM_HOME} && \  
apk add \--no-cache \--virtual=.build-deps curl && \  
curl -L ${DIST_MIRROR}/download/v${VERSION}/sam_${VERSION}_linux_amd64.tar.gz
| tar xvz -C /usr/local/bin && \  
rm -f *.tar.gz && \  
apk del .build-deps && \  
apk add \--no-cache py-pip && pip install awscli  
WORKDIR ${SAM_HOME}  
ENTRYPOINT ["/usr/local/bin/sam"]  

