FROM openjdk:8-jdk  
  
ENV GRADLE_HOME /opt/gradle  
ENV GRADLE_VERSION 4.8  
RUN set -o errexit -o nounset \  
&& echo "Downloading Gradle" \  
&& wget -O gradle.zip
"https://services.gradle.org/distributions/gradle-${GRADLE_VERSION}-bin.zip" \  
\  
&& echo "Installing Gradle" \  
&& unzip gradle.zip \  
&& rm gradle.zip \  
&& mv "gradle-${GRADLE_VERSION}" "${GRADLE_HOME}/" \  
&& ln -s "${GRADLE_HOME}/bin/gradle" /usr/bin/gradle \  
\  
&& mkdir /root/.gradle  
  
CMD ["gradle"]  

