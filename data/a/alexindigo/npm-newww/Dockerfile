# alexindigo/npm-newww  
FROM alexindigo/node-app  
MAINTAINER Alex Indigo <iam@alexindigo.com>  
  
ENV NEWWW_VERSION v2.1.0  
# Escape volume  
RUN mkdir -p /var/www  
WORKDIR /var/www  
  
# Install gulp  
RUN npm install -g gulp  
  
# Extract latest newww into working directory  
RUN curl -L -s https://github.com/npm/newww/archive/${NEWWW_VERSION}.tar.gz -o
/tmp/newww-${NEWWW_VERSION}.tar.gz && \  
tar -C . --strip-components 1 -xzf /tmp/newww-${NEWWW_VERSION}.tar.gz && \  
rm /tmp/newww-${NEWWW_VERSION}.tar.gz  
  
# Install dependencies  
RUN npm install  
  
# Build assets  
RUN gulp build  

