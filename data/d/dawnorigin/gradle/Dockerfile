FROM openjdk:8-jdk  
  
CMD ["gradle"]  
  
ENV GRADLE_HOME /opt/gradle  
ENV GRADLE_VERSION 2.14.1  
ARG
GRADLE_DOWNLOAD_SHA256=cfc61eda71f2d12a572822644ce13d2919407595c2aec3e3566d2aab6f97ef39  
RUN set -o errexit -o nounset \  
&& echo "Downloading Gradle" \  
&& wget --no-verbose --output-document=gradle.zip
"https://services.gradle.org/distributions/gradle-${GRADLE_VERSION}-bin.zip" \  
\  
&& echo "Checking download hash" \  
&& echo "${GRADLE_DOWNLOAD_SHA256} *gradle.zip" | sha256sum --check - \  
\  
&& echo "Installing Gradle" \  
&& unzip gradle.zip \  
&& rm gradle.zip \  
&& mv "gradle-${GRADLE_VERSION}" "${GRADLE_HOME}/" \  
&& ln --symbolic "${GRADLE_HOME}/bin/gradle" /usr/bin/gradle \  
\  
&& echo "Creating Gradle cache for root" \  
&& mkdir /root/.gradle \  
\  
&& echo "Adding gradle user and group" \  
&& groupadd --system --gid 1000 gradle \  
&& useradd --system --gid gradle --uid 1000 --shell /bin/bash --create-home
gradle \  
&& mkdir /home/gradle/.gradle \  
&& chown --recursive gradle:gradle /home/gradle  
  
# Create root .gradle volume  
VOLUME "/root/.gradle"  
  
# Create gradle .gradle volume  
USER gradle  
VOLUME "/home/gradle/.gradle"  
WORKDIR /home/gradle  
  
RUN set -o errexit -o nounset \  
&& echo "Testing Gradle installation" \  
&& gradle --version

