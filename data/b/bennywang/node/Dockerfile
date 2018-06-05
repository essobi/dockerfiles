FROM node:8-alpine  
  
ENV NPM_CONFIG_LOGLEVEL error  
ENV YARN_VERSION 0.27.5  
# Install Yarn  
ADD https://yarnpkg.com/downloads/$YARN_VERSION/yarn-v${YARN_VERSION}.tar.gz
/opt/yarn.tar.gz  
RUN cd /opt/ && \  
tar xf yarn.tar.gz && \  
mv dist yarn && \  
rm yarn.tar.gz  
ENV PATH $PATH:/opt/yarn/bin/  
  
# Install AWS CLI  
RUN apk --no-cache update && \  
apk --no-cache add python py-pip py-setuptools ca-certificates groff less && \  
pip --no-cache-dir install awscli && \  
rm -rf /var/cache/apk/*  
  
# Install development packages  
RUN apk add --no-cache --update bash curl git openssh jq && \  
rm -rf /var/cache/apk/*  

