# alexindigo/npm-registry-couchapp  
FROM alexindigo/node-dev:0.10.29  
MAINTAINER Alex Indigo <iam@alexindigo.com>  
  
# Settings  
ENV NPMJS_VERSION 2.4.3  
ENV NPMJS_URL https://github.com/npm/npm-registry-
couchapp/archive/v${NPMJS_VERSION}.tar.gz  
  
# Get NPM registry app  
RUN mkdir -p /opt/npmjs && \  
curl -s -L -o /opt/npmjs.tar.gz ${NPMJS_URL} && \  
tar -C /opt/npmjs --strip-components 1 -xzf /opt/npmjs.tar.gz && \  
rm /opt/npmjs.tar.gz  
  
# Build NPM registry app  
RUN cd /opt/npmjs && \  
npm install  
  
# Make dependencies available as standalone apps  
RUN ln -s /opt/npmjs/node_modules/.bin/couchapp /usr/local/bin/couchapp && \  
ln -s /opt/npmjs/node_modules/.bin/json /usr/local/bin/json  
  
# Remove unnecessary dependencies and checks  
RUN sed -i'' 's/`git describe --tags`/v'${NPMJS_VERSION}'/' /opt/npmjs/push.sh
&& \  
sed -i'' '/-k -u "$auth"/d' /opt/npmjs/copy.sh  
  
# Add init script  
ADD ./init.sh /opt/npmjs/couchdb_init.sh  
  
WORKDIR /opt/npmjs  
  
# init npm couchapp  
CMD ["/opt/npmjs/couchdb_init.sh"]  

