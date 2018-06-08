FROM noumia/jre8  
  
ENV GRADLE_VER=4.2 GRADLE_HOME=/opt/gradle PATH=/opt/gradle/bin:${PATH}  
  
RUN set -x \  
&& apt-get update && apt-get install -y unzip \  
&& export GRADLE_NAME="gradle-${GRADLE_VER}-bin.zip" \  
&& export
GRADLE_URL="https://downloads.gradle.org/distributions/${GRADLE_NAME}" \  
&& cd /opt \  
&& curl -fsSLO "${GRADLE_URL}" \  
&& unzip "${GRADLE_NAME}" \  
&& mv "gradle-${GRADLE_VER}" gradle \  
&& mkdir -p /workspace \  
&& mkdir -p /root/.gradle \  
&& echo "org.gradle.daemon=false" > /root/.gradle/gradle.properties \  
&& rm "${GRADLE_NAME}" \  
&& rm -rf /var/lib/apt/lists/*  
  
WORKDIR /workspace  
  
ENTRYPOINT [ "gradle" ]  

