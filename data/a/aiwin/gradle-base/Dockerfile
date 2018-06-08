FROM openjdk:8-jdk  
  
LABEL maintainer="javier.boo@aiwin.es"  
  
ARG USER_HOME_DIR="/root"  
ARG GRADLE_VERSION="4.0.1"  
ARG
GRADLE_DOWNLOAD_SHA256=d717e46200d1359893f891dab047fdab98784143ac76861b53c50dbd03b44fd4  
  
RUN apt-get update && apt-get install -y jq zip python git  
  
RUN curl "https://bootstrap.pypa.io/get-pip.py" -o "/tmp/get-pip.py" && \  
python /tmp/get-pip.py && \  
pip install awscli --ignore-installed six  
  
ENV GRADLE_HOME /opt/gradle  
ENV GRADLE_USER_HOME "$USER_HOME_DIR/.gradle"  
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
&& ln --symbolic "${GRADLE_HOME}/bin/gradle" /usr/bin/gradle  
  
RUN git clone https://github.com/aiwin-tools/devops-scripts.git
"$HOME/scripts"  
  
VOLUME "$USER_HOME_DIR/.gradle"  
  
ADD sonarqube.gradle $GRADLE_HOME  
  
CMD ["gradle"]  

