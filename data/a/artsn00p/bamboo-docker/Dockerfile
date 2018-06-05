FROM openjdk:8-alpine  
  
MAINTAINER Artem Silenkov <artem.silenkov@gmail.com>  
  
# Setup useful environment variables  
ENV BAMBOO_HOME /var/atlassian/bamboo  
ENV BAMBOO_INSTALL /opt/atlassian/bamboo  
ENV BAMBOO_VERSION 6.4.0  
ENV KUBECONFIG /var/atlassian/bamboo/.kube/config  
  
# Install Atlassian Bamboo and helper tools and setup initial home  
# directory structure.  
RUN set -x \  
&& apk add --no-cache curl xmlstarlet git openssh bash \  
&& mkdir -p "${BAMBOO_HOME}/lib" \  
&& chmod -R 700 "${BAMBOO_HOME}" \  
&& mkdir -p "${BAMBOO_INSTALL}" \  
&& curl -Ls
"https://www.atlassian.com/software/bamboo/downloads/binary/atlassian-
bamboo-${BAMBOO_VERSION}.tar.gz" | tar -zx --directory "${BAMBOO_INSTALL}"
\--strip-components=1 --no-same-owner \  
&& curl -Ls "https://dev.mysql.com/get/Downloads/Connector-J/mysql-connector-
java-5.1.40.tar.gz" | tar -xz --directory "${BAMBOO_INSTALL}/lib" \--strip-
components=1 --no-same-owner "mysql-connector-java-5.1.40/mysql-connector-
java-5.1.40-bin.jar" \  
&& chmod -R 700 "${BAMBOO_INSTALL}" \  
&& sed --in-place 's/^# umask 0027$/umask 0027/g'
"${BAMBOO_INSTALL}/bin/setenv.sh" \  
&& xmlstarlet ed --inplace \  
\--delete "Server/Service/Engine/Host/@xmlValidation" \  
\--delete "Server/Service/Engine/Host/@xmlNamespaceAware" \  
"${BAMBOO_INSTALL}/conf/server.xml" \  
&& touch -d "@0" "${BAMBOO_INSTALL}/conf/server.xml"  
  
# Install requirements for kubectl  
RUN apk add -U openssl tar gzip ca-certificates && \  
wget -q -O /etc/apk/keys/sgerrand.rsa.pub
https://raw.githubusercontent.com/sgerrand/alpine-pkg-
glibc/master/sgerrand.rsa.pub && \  
wget https://github.com/sgerrand/alpine-pkg-
glibc/releases/download/2.23-r3/glibc-2.23-r3.apk && \  
apk add glibc-2.23-r3.apk && \  
rm glibc-2.23-r3.apk  
  
# Install kubectl  
RUN curl -L -o /usr/bin/kubectl https://storage.googleapis.com/kubernetes-
release/release/v1.8.0/bin/linux/amd64/kubectl && \  
chmod +x /usr/bin/kubectl  
  
USER root:root  
  
# Create kubectl config directory  
RUN mkdir /var/atlassian/bamboo/.kube  
  
# Expose default HTTP and SSH ports.  
EXPOSE 8085 54663  
# Set volume mount points for installation and home directory. Changes to the  
# home directory needs to be persisted as well as parts of the installation  
# directory due to eg. logs.  
VOLUME ["/var/atlassian/bamboo","/opt/atlassian/bamboo/logs"]  
  
# Set the default working directory as the Bamboo home directory.  
WORKDIR /var/atlassian/bamboo  
  
COPY "docker-entrypoint.sh" "/"  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
# Run Atlassian Bamboo as a foreground process by default.  
CMD ["/opt/atlassian/bamboo/bin/start-bamboo.sh", "-fg"]  

