FROM node:10.4-stretch  
LABEL maintainer "David J. M. Karlsen <david@davidkarlsen.com>"  
ENV ANGULAR_CLI_VERSION=6.0.7 OWASP_DEPENDENCY_CHECK_VERSION=3.2.1
SONAR_CLI_VERSION=3.2.0.1227 YARN_VERSION=1.7.0  
  
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-
key add - && \  
apt-get update && apt-get -y install apt-transport-https && \  
sh -c 'echo "deb [arch=amd64] https://dl.google.com/linux/chrome/deb/ stable
main" >> /etc/apt/sources.list.d/google.list' && \  
apt-get update && \  
apt-get -y install google-chrome-stable vim less psmisc zip unzip net-tools
libdbus-glib-1-2 && \  
apt-get -y dist-upgrade && \  
apt-get clean && \  
rm -rf /var/cache/apt && \  
arch="$(dpkg --print-architecture | awk -F- '{ print $NF }')" && \  
wget -O /usr/local/bin/gosu
"https://github.com/tianon/gosu/releases/download/1.10/gosu-$arch" && \  
chmod a+x /usr/local/bin/gosu && \  
wget -q -O - "https://download.mozilla.org/?product=firefox-latest-
ssl&os=linux64" |tar xjv -C /opt && \  
yarn global add @angular/cli@${ANGULAR_CLI_VERSION} sonarqube-scanner@latest
stylelint && \  
ng set \--global packageManager=yarn && \  
wget https://dl.bintray.com/jeremy-long/owasp/dependency-
check-${OWASP_DEPENDENCY_CHECK_VERSION}-release.zip -O /tmp/owasp-dep-
check.zip && \  
unzip /tmp/owasp-dep-check.zip -d /usr/local && \  
rm /tmp/owasp-dep-check.zip && \  
wget https://sonarsource.bintray.com/Distribution/sonar-scanner-cli/sonar-
scanner-cli-${SONAR_CLI_VERSION}-linux.zip -O /tmp/sonar.zip && \  
mkdir -p /home/node/.sonar/native-sonar-scanner && \  
unzip /tmp/sonar.zip -d /home/node/.sonar/native-sonar-scanner && \  
rm /tmp/sonar.zip && \  
wget
https://yarnpkg.com/downloads/${YARN_VERSION}/yarn-v${YARN_VERSION}.tar.gz -O
-|tar xzvf - -C /opt && \  
ln -sf /opt/yarn-v${YARN_VERSION}/bin/yarn /usr/local/bin/yarn && \  
ln -sf /opt/yarn-v${YARN_VERSION}/bin/yarnpkg /usr/local/bin/yarnpkg  
  
ENV PROXY=http://proxy.evry.com:8080 \  
proxy=http://proxy.evry.com:8080 \  
HTTPS_PROXY=http://proxy.evry.com:8080 \  
https_proxy=http://proxy.evry.com:8080 \  
NO_PROXY=localhost,.evry.com,.finods.com,.localdomain,.cosng.net \  
NPM_REGISTRY=https://fsnexus.evry.com/nexus/repository/npm-all/ \  
CHROME_BIN=/usr/bin/google-chrome \  
NPM_CONFIG_PREFIX=/home/node/.npm-global \  
PATH="/opt/firefox:/usr/local/dependency-check/bin:${PATH}" \  
GOSU_USER="0:0" \  
GOSU_CHOWN="/home/node /usr/local/dependency-check/data" \  
PUPPETEER_SKIP_CHROMIUM_DOWNLOAD=true \  
JAVA_HOME=/home/node/.sonar/native-sonar-scanner/sonar-
scanner-${SONAR_CLI_VERSION}-linux/jre  
  
RUN /usr/local/dependency-check/bin/dependency-check.sh \--updateonly && \  
npm set registry ${NPM_REGISTRY} && \  
yarn config set registry ${NPM_REGISTRY} && \  
chown -R node:node /home/node /usr/local/dependency-check/data && \  
chmod -R a+w /usr/local/dependency-check/data  
  
COPY gosu-entrypoint.sh showversions.sh /  
#RUN chmod +x /gosu-entrypoint.sh && \  
# /showversions.sh  
RUN chmod +x /gosu-entrypoint.sh  
  
ENTRYPOINT ["/gosu-entrypoint.sh"]  

