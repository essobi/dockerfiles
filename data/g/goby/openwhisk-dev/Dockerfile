FROM java:8-jdk  
  
MAINTAINER "goby<goby@foxmail.com>"  
ENV SCALA_HOME /usr/local/share/scala  
ENV SCALA_VERSION 2.11.6  
ENV PATH $PATH:$SCALA_HOME/bin  
  
ENV GRADLE_HOME /opt/gradle  
ENV GRADLE_VERSION 3.5  
RUN set -o errexit -o nounset && \  
echo "Installing scala" && \  
wget --quiet
http://downloads.lightbend.com/scala/$SCALA_VERSION/scala-$SCALA_VERSION.tgz
&& \  
tar -xf scala-$SCALA_VERSION.tgz && \  
rm scala-$SCALA_VERSION.tgz && \  
mv scala-$SCALA_VERSION $SCALA_HOME && \  
\  
echo "Installing pip and ansible" && \  
apt-get update && apt-get install -y python-pip python-dev libffi-dev libssl-
dev && \  
pip install jsonschema && \  
pip install argcomplete && \  
pip install couchdb && \  
pip install markupsafe && \  
pip install --upgrade cffi && \  
pip install ansible==2.3.0.0 && \  
pip install docker==2.2.1 && \  
\  
echo "Downloading Gradle" && \  
wget --no-verbose --output-document=gradle.zip
"https://services.gradle.org/distributions/gradle-${GRADLE_VERSION}-bin.zip"
&& \  
\  
echo "Installing Gradle" && \  
unzip gradle.zip && \  
rm gradle.zip && \  
mv "gradle-${GRADLE_VERSION}" "${GRADLE_HOME}/" && \  
ln --symbolic "${GRADLE_HOME}/bin/gradle" /usr/bin/gradle && \  
\  
echo "Adding whisk user and group" && \  
groupadd --system --gid 1000 whisk && \  
useradd --system --gid whisk --uid 1000 --shell /bin/bash --create-home whisk
&& \  
mkdir /home/whisk/.gradle && \  
chown --recursive whisk:whisk /home/whisk  
  
VOLUME "/home/whisk/.gradle"  
VOLUME /home/whisk/dev/openwhisk  
WORKDIR /home/whisk/dev/openwhisk  

