FROM manabugt/android  
#FROM beevelop/android-nodejs:v4  
ENV NODEJS_VERSION 5.3.0  
ENV CORDOVA_VERSION 5.4.1  
ENV IONIC_CLI_VERSION 1.7.12  
ENV MIONIC_VERSION 1.5.0  
ENV NODE_MODULES_DIR node_modules  
ENV BOWER_CLIENT_ID 896698526080  
ENV BOWER_DIR app/bower_components  
  
# zipalign  
ENV PATH $PATH:/opt/android-sdk-linux/build-tools/23.0.1  
RUN which zipalign  
  
RUN apt-get update -y && \  
apt-get install -y \  
git \  
python \  
unzip \  
build-essential \  
openssh-client && \  
type git && \  
type python && \  
type unzip && \  
type make && \  
type ssh-keyscan && \  
apt-get clean  
  
# NODEJS  
# Set Environment Variables  
ENV PATH $PATH:/opt/nodejs/bin  
WORKDIR "/opt"  
RUN curl -O
https://nodejs.org/dist/v${NODEJS_VERSION}/node-v${NODEJS_VERSION}-linux-x64.tar.gz
&& \  
# Extract and move to /opt  
tar xf node-v${NODEJS_VERSION}-linux-x64.tar.gz && \  
mv node-v${NODEJS_VERSION}-linux-x64 /opt/nodejs && \  
  
# Clean up  
rm node-v${NODEJS_VERSION}-linux-x64.tar.gz  
  
RUN npm install --global \  
bower \  
generator-m-ionic@${MIONIC_VERSION} \  
gulp \  
ionic@$IONIC_CLI_VERSION \  
yo \  
cordova@${CORDOVA_VERSION}  
  
EXPOSE 3000  
EXPOSE 3001  
COPY docker-entrypoint-development.sh /  
COPY build-release.sh /  
  
VOLUME /appm  
  
RUN useradd -ms /bin/bash app  
RUN chown -R app /opt  
  
USER app  
WORKDIR /home/app  
RUN mkdir -p .config/configstore  
RUN echo '{"clientId": '$BOWER_CLIENT_ID',"optOut": true}' >
.config/configstore/insight-yo.json  
RUN echo 'clientId: '$BOWER_CLIENT_ID >> .config/configstore/insight-bower.yml  
RUN echo 'optOut: true' >> .config/configstore/insight-bower.yml  
  
# github known_hosts  
# Add github.com to known_hosts  
RUN mkdir -p .ssh && \  
ssh-keyscan -H github.com >> .ssh/known_hosts  
  
RUN echo 'umask 000' >> .bashrc  
  
WORKDIR /appm  
  
ENTRYPOINT ["/docker-entrypoint-development.sh"]  
CMD ["gulp", "watch", "--no-open"]  

