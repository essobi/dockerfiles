#  
# Builds the STOIC redirector image  
#  
# https://github.com/sutoiku/stoic.redirector 'docker' branch  
#  
FROM node:slim  
MAINTAINER Stoic Team <devops@sutoiku.com>  
  
# Install a stoic.redirector build from aws  
RUN \  
cd /tmp && \  
STOIC_REDIRECTOR_VERSION=1.1 && \  
STOIC_REDIRECTOR_TGZ=${STOIC_REDIRECTOR_VERSION}.tar.gz && \  
STOIC_REDIRECTOR_DIR=/app/stoic.redirector-${STOIC_REDIRECTOR_VERSION} && \  
wget
https://github.com/sutoiku/stoic.redirector/archive/${STOIC_REDIRECTOR_TGZ} &&
\  
mkdir -p /app && \  
cd /app && \  
tar xzf /tmp/${STOIC_REDIRECTOR_TGZ} && \  
mv ${STOIC_REDIRECTOR_DIR}/* /app/ && \  
rm -rf ${STOIC_REDIRECTOR_DIR} && \  
npm install > npm.log 2>&1 && \  
rm -rf /tmp/*  
  
ENV DEBUG redirector  
WORKDIR /app  
EXPOSE 2929  
CMD ["node", "index.js"]  

