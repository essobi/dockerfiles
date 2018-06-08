ARG BASE_IMAGE_TAG  
  
ARG JENKINS_HOME=/home/jenkins  
  
FROM jenkins/jenkins:${BASE_IMAGE_TAG}  
  
ARG JENKINS_VER  
  
ENV JENKINS_VER $JENKINS_VER  
ENV JENKINS_HOME $JENKINS_HOME  
  
# Skip initial jenkins setup  
ENV JAVA_OPTS "-Djenkins.install.runSetupWizard=false"  
ENV JENKINS_USER admin  
ENV JENKINS_EXECUTORS 2  
USER jenkins  
  
COPY rootfs/ /  
  
USER root  
  
RUN set -ex; \  
\  
adduser jenkins ping; \  
\  
apk add --no-cache \  
curl \  
docker \  
make \  
pwgen \  
su-exec \  
sudo \  
tar \  
wget; \  
\  
# Script to fix volumes permissions via sudo.  
echo "chown jenkins:jenkins ${JENKINS_HOME}" > /usr/local/bin/init_volumes; \  
chmod +x /usr/local/bin/init_volumes; \  
echo 'jenkins ALL=(root) NOPASSWD:SETENV: /usr/local/bin/init_volumes' >
/etc/sudoers.d/jenkins  
  
  
RUN /usr/local/bin/install-plugins.sh < /usr/share/jenkins/ref/plugins.txt  
  
USER jenkins  
  
COPY \--from=composer:latest /usr/bin/composer /usr/bin/composer  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
CMD ["/sbin/tini", "--", "/usr/local/bin/jenkins.sh"]  

