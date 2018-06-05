FROM gradle:jdk-alpine  
  
LABEL maintainer="Mathieu BRUNOT <mathieu.brunot@monogramm.io>"  
  
ENV ADK_VERSION 4.1.8  
ENV AXELOR_HOME /opt/adk  
  
# Switch to root  
USER root  
  
# Get axelor-development-kit  
RUN set -o errexit -o nounset ; \  
echo "Installing needed packages"; \  
apk add --no-cache tar bash; \  
\  
echo "Downloading Axelor Development Kit"; \  
wget -O adk.tar.gz https://github.com/axelor/axelor-development-
kit/archive/v${ADK_VERSION}.tar.gz; \  
\  
echo "Building Axelor Development Kit"; \  
tar -xzf adk.tar.gz; \  
rm adk.tar.gz; \  
mkdir -p /usr/src; \  
mv "axelor-development-kit-${ADK_VERSION}" "/usr/src/adk"; \  
cd "/usr/src/adk/"; \  
./gradlew build; \  
\  
echo "Installing Axelor Development Kit"; \  
tar -xzf "/usr/src/adk/build/distributions/axelor-development-
kit-${ADK_VERSION}.tgz"; \  
mv "axelor-development-kit-${ADK_VERSION}" "${AXELOR_HOME}"; \  
chown -R gradle "${AXELOR_HOME}/"; \  
./gradlew clean; \  
export PATH=$AXELOR_HOME/bin:$PATH; \  
ln -s "${AXELOR_HOME}/bin/axelor" /usr/bin/axelor  
  
# Switch back to gradle user  
USER gradle  
WORKDIR /home/gradle  
  
# Test axelor-development-kit  
RUN set -o errexit -o nounset; \  
echo "Testing Axelor Development Kit installation"; \  
axelor --version  
  
CMD ["axelor"]  

