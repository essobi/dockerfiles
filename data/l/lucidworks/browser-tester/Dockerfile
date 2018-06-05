FROM debian:testing  
  
ENV VERSION=6.9.5 NPM_VERSION=3.8 \  
DEBIAN_FRONTEND=noninteractive \  
NVM_DIR="/root/.nvm"  
# stop dkpg from installing docs  
COPY /protractor/etc/dkpg/dpkg.cfg.d/01_nodoc /etc/dkpg/dpkg.cfg.d/01_nodoc  
  
RUN apt-get update && \  
apt-get install -y \  
openjdk-8-jre \  
xvfb \  
libgconf-2-4 \  
libexif12 \  
chromium \  
supervisor \  
netcat-traditional \  
curl && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* && \  
rm -rf /var/log/*  
  
#==============  
# libav/avconv  
#==============  
# Layer size: medium: 11.58 MB (with --no-install-recommends)  
# Layer size: medium: 16.75 MB  
# libav-tools (avconv): a fork of ffmpeg  
# a better alternative to Pyvnc2swf  
# (use in Ubuntu <= 14) packages: libav-tools libx264-142  
RUN apt -qqy update \  
&& apt -qqy --no-install-recommends install \  
libav-tools \  
&& rm -rf /var/lib/apt/lists/* \  
&& apt -qyy clean  
  
#========  
# ffmpeg  
#========  
# MP4Box (gpac) to clean the video credits to @taskworld @dtinth  
# ffmpeg (ffmpeg): Is a better alternative to Pyvnc2swf  
# (use in Ubuntu >= 15) packages: ffmpeg  
# Layer size: medium: ~12 MB (with --no-install-recommends)  
# Layer size: medium: ~17 MB  
RUN apt -qqy update \  
&& apt -qqy install \  
ffmpeg \  
gpac \  
&& rm -rf /var/lib/apt/lists/* \  
&& apt -qyy clean  
  
# Add main configuration file  
ADD protractor/supervisor.conf /etc/supervisor/supervisor.conf  
  
# Add service defintions  
ADD protractor/supervisord/protractor.conf /etc/supervisor/conf.d/  
  
# ADD protractor/package.json /project/package.json  
ADD protractor/install_nvm.sh /project/install_nvm.sh  
ADD protractor/bin/protractor/run_protractor.sh
/bin/protractor/run_protractor.sh  
  
# https://www.liquidweb.com/kb/how-to-install-nvm-node-version-manager-for-
node-js-on-ubuntu-12-04-lts/  
RUN /bin/bash -c "/project/install_nvm.sh && rm -f /project/install_nvm.sh"  
  
ENV PATH
"$PATH:/root/.nvm/versions/node/v6.9.5/lib/node_modules/integration/node_modules/webdriver-
manager"  
RUN /bin/bash -c ". \"$NVM_DIR/nvm.sh\" && \  
nvm install $VERSION; nvm use v$VERSION; \  
cd /project; \  
npm install --global webdriver-manager \  
webdriver-manager \  
lodash \  
protractor \  
request-promise \  
jasmine-core@2.3.4 \  
jasmine-reporters@2.0.7 \  
jasmine-spec-reporter@3.2.0 \  
q@~1.5.0 \  
oauth-redirect@1.0.0 \  
request \  
npm-install-missing \  
optimist; \  
webdriver-manager update && \  
npm bin && \  
echo 'npm:'; npm -v; \  
echo 'node:'; node -v; \  
find / -name lodash; \  
echo 'path: $PATH'; \  
echo 'NODE_PATH: $NODE_PATH'; \  
echo 'NVM_DIR: $NVM_DIR'; \  
which protractor; protractor --version; \  
chmod +x /bin/protractor/run_protractor.sh"  
  
RUN /bin/bash -c ". \"$NVM_DIR/nvm.sh\" && nvm use v$VERSION; npm bin; find /
-name protractor | grep '\\.bin'; which protractor; protractor --version"  
  
# Container's entry point, executing supervisord in the foreground  
# CMD [ "/usr/bin/supervisord", "-n", "-c", "/etc/supervisor/supervisor.conf"]  
ENTRYPOINT ["/bin/bash", "-c", ". \"$NVM_DIR/nvm.sh\" && nvm use v$VERSION &&
/usr/bin/supervisord -n -c /etc/supervisor/supervisor.conf"]  
  
# Protractor test project needs to be mounted at /project  
VOLUME ["/project"]  

