FROM ubuntu:wily  
  
RUN apt-get update &&\  
apt-get install -y openjdk-8-jdk wget git curl sudo zip python2.7-dev python-
pip libfreetype6-dev bash-completion libsdl1.2debian libfdt1 libpixman-1-0
libglib2.0-dev &&\  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ENV JENKINS_HOME /var/jenkins_home  
ENV JENKINS_VERSION 1.623  
ENV JENKINS_SHA db873da98bddcea47e815442e28f1164442efd5a  
ENV JENKINS_UC https://updates.jenkins-ci.org  
  
ENV PEBBLE_SDK_VERSION pebble-sdk-4.4-linux64  
  
# get pebble tool  
RUN mkdir -p /opt/pebble-dev  
RUN curl -sSL https://s3.amazonaws.com/assets.getpebble.com/pebble-
tool/${PEBBLE_SDK_VERSION}.tar.bz2 \  
| tar -v -C /opt/pebble-dev/ -xj  
  
# prepare python environment for Pebble  
WORKDIR /opt/pebble-dev/${PEBBLE_SDK_VERSION}  
RUN /bin/bash -c " \  
pip install virtualenv && \  
virtualenv --no-site-packages .env && \  
source .env/bin/activate && \  
pip install -r requirements.txt && \  
deactivate " && \  
rm -r /root/.cache/  
  
# Jenkins is ran with user `jenkins`, uid = 1000  
# If you bind mount a volume from host/vloume from a data container,  
# ensure you use same uid  
RUN useradd -d "$JENKINS_HOME" -u 1000 -m -s /bin/bash jenkins  
RUN chmod +w /etc/sudoers &&\  
echo "jenkins ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers &&\  
chmod -w /etc/sudoers &&\  
chmod -R 777 /opt/pebble-dev/  
  
# Jenkins home directoy is a volume, so configuration and build history  
# can be persisted and survive image upgrades  
VOLUME /var/jenkins_home  
  
# `/usr/share/jenkins/ref/` contains all reference configuration we want  
# to set on a fresh new installation. Use it to bundle additional plugins  
# or config file with your custom jenkins Docker image.  
RUN mkdir -p /usr/share/jenkins/ref/init.groovy.d  
# disable pebble analytics in the ref  
RUN mkdir -p /usr/share/jenkins/ref/.pebble-sdk/ && \  
touch /usr/share/jenkins/ref/.pebble-sdk/ACCEPT_LICENSE &&\  
touch /usr/share/jenkins/ref/.pebble-sdk/NO_TRACKING  
  
# install the plugins listed in the plugins txt  
COPY plugins.sh /usr/local/bin/plugins.sh  
COPY plugins.txt /plugins.txt  
RUN plugins.sh /plugins.txt  
  
# Use tini as subreaper in Docker container to adopt zombie processes  
RUN curl -fL https://github.com/krallin/tini/releases/download/v0.5.0/tini-
static -o /bin/tini && chmod +x /bin/tini  
  
COPY init.groovy /usr/share/jenkins/ref/init.groovy.d/tcp-slave-agent-
port.groovy  
  
# could use ADD but this one does not check Last-Modified header  
# see https://github.com/docker/docker/issues/8331  
RUN curl -fL http://mirrors.jenkins-ci.org/war/$JENKINS_VERSION/jenkins.war -o
/usr/share/jenkins/jenkins.war \  
&& echo "$JENKINS_SHA /usr/share/jenkins/jenkins.war" | sha1sum -c -  
  
RUN chown -R jenkins "$JENKINS_HOME" /usr/share/jenkins/ref  
  
# for main web interface:  
EXPOSE 8080  
# will be used by attached slave agents:  
EXPOSE 50000  
ENV COPY_REFERENCE_FILE_LOG $JENKINS_HOME/copy_reference_file.log  
  
USER jenkins  
  
# set PATH  
ENV PATH /opt/pebble-
dev/${PEBBLE_SDK_VERSION}/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin  
  
COPY jenkins.sh /usr/local/bin/jenkins.sh  
ENTRYPOINT ["/bin/tini", "--", "/usr/local/bin/jenkins.sh"]  
  

