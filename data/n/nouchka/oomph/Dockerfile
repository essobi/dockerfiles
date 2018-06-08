ARG BASE_IMAGE=ubuntu:xenial  
FROM ${BASE_IMAGE}  
LABEL maintainer="Jean-Avit Promis docker@katagena.com"  
  
ARG ECLIPSE_OOMPH_INSTALLER_TAR_URL=http://ftp-stud.fht-
esslingen.de/pub/Mirrors/eclipse/oomph/products/eclipse-inst-linux64.tar.gz  
ENV ECLIPSE_OOMPH_INSTALLER_DIRECTORY=/opt  
ARG PUID=1000  
ARG PGID=1000  
ARG BASE_IMAGE=ubuntu:xenial  
ARG DOCKER_TAG=php7  
LABEL version="${DOCKER_TAG}"  
  
ENV PUID ${PUID}  
ENV PGID ${PGID}  
  
RUN apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get -yq install wget git libcanberra-
gtk3-module ssh-askpass openssh-client wmctrl && \  
[ "$DOCKER_TAG" != "php7" ] || apt-get -yq install openjdk-8-jdk php7.0 php-
cli php-xdebug php-intl php-xml && \  
[ "$DOCKER_TAG" != "php5" ] || apt-get -yq install openjdk-7-jdk php5 php5-cli
php5-xdebug && \  
[ "$DOCKER_TAG" != "latest" ] || apt-get -yq install openjdk-8-jdk && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \  
wget "${ECLIPSE_OOMPH_INSTALLER_TAR_URL}" -O /tmp/eclipse-inst.tar.gz -q && \  
tar -xf /tmp/eclipse-inst.tar.gz -C ${ECLIPSE_OOMPH_INSTALLER_DIRECTORY} && \  
rm /tmp/eclipse-inst.tar.gz && \  
[ "$DOCKER_TAG" = "latest" ] || wget "http://get.sensiolabs.org/php-cs-
fixer.phar" -O php-cs-fixer && \  
[ "$DOCKER_TAG" = "latest" ] || chmod a+x php-cs-fixer && \  
[ "$DOCKER_TAG" = "latest" ] || mv php-cs-fixer /usr/local/bin/php-cs-fixer &&
\  
[ "$DOCKER_TAG" = "latest" ] || wget -qO- https://getcomposer.org/installer |
php -- --install-dir=/usr/local/bin --filename=composer && \  
[ "$DOCKER_TAG" = "latest" ] || php /usr/local/bin/composer self-update  
  
COPY launch.sh /launch.sh  
COPY user.setup
/home/developer/.eclipse/org.eclipse.oomph.setup/setups/user.setup  
  
RUN export uid=${PUID} gid=${PGID} && \  
mkdir -p /home/developer/workspace && \  
mkdir -p /home/developer/.p2/pool/ && \  
echo "developer:x:${uid}:${gid}:Developer,,,:/home/developer:/bin/bash" >>
/etc/passwd && \  
echo "developer:x:${uid}:" >> /etc/group && \  
chmod +x /launch.sh && \  
chown developer: /launch.sh && \  
chown -R developer: /${ECLIPSE_OOMPH_INSTALLER_DIRECTORY}/ && \  
mkdir -p /home/developer/eclipse/ && \  
chown -R developer: /home/developer/ && \  
chown ${uid}:${gid} -R /home/developer  
  
USER developer  
ENV HOME /home/developer  
VOLUME /home/developer/eclipse/ /opt/eclipse-installer/
/home/developer/.p2/pool/  
  
CMD /launch.sh  

