FROM area51/node  
MAINTAINER Peter Mount <peter@retep.org>  
  
ENV JENKINS_HOME /home/jenkins  
  
ENV JAVA_VERSION_MAJOR 8  
ENV JAVA_VERSION_MINOR 131  
ENV JAVA_VERSION_BUILD 11  
ENV JAVA_PACKAGE server-jre  
ENV URL_ELEMENT d54c1d3a095b4ff2b6607d096fa80163  
  
ENV PATH $PATH:/opt/jdk/bin  
  
RUN apk add --update \  
ca-certificates \  
openssh \  
curl \  
git \  
mercurial \  
subversion &&\  
rm -rf /var/cache/apk/*  
  
COPY keys/* /etc/ssh.cache/  
  
COPY scripts/*.sh /  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
# Download and add the pem to the trust store  
RUN mkdir -p /opt &&\  
curl -sjkLH "Cookie: oraclelicense=accept-securebackup-cookie" \  
-o java.tar.gz \  
http://download.oracle.com/otn-
pub/java/jdk/${JAVA_VERSION_MAJOR}u${JAVA_VERSION_MINOR}-b${JAVA_VERSION_BUILD}/${URL_ELEMENT}/${JAVA_PACKAGE}-${JAVA_VERSION_MAJOR}u${JAVA_VERSION_MINOR}-linux-x64.tar.gz
&&\  
gunzip -c java.tar.gz | tar -xf - -C /opt && rm -f java.tar.gz &&\  
ln -s /opt/jdk1.${JAVA_VERSION_MAJOR}.0_${JAVA_VERSION_MINOR} /opt/jdk &&\  
rm -rf /opt/jdk/*src.zip \  
/opt/jdk/lib/missioncontrol \  
/opt/jdk/lib/visualvm \  
/opt/jdk/lib/*javafx* \  
/opt/jdk/jre/lib/plugin.jar \  
/opt/jdk/jre/lib/ext/jfxrt.jar \  
/opt/jdk/jre/bin/javaws \  
/opt/jdk/jre/lib/javaws.jar \  
/opt/jdk/jre/lib/desktop \  
/opt/jdk/jre/plugin \  
/opt/jdk/jre/lib/deploy* \  
/opt/jdk/jre/lib/*javafx* \  
/opt/jdk/jre/lib/*jfx* \  
/opt/jdk/jre/lib/amd64/libdecora_sse.so \  
/opt/jdk/jre/lib/amd64/libprism_*.so \  
/opt/jdk/jre/lib/amd64/libfxplugins.so \  
/opt/jdk/jre/lib/amd64/libglass.so \  
/opt/jdk/jre/lib/amd64/libgstreamer-lite.so \  
/opt/jdk/jre/lib/amd64/libjavafx*.so \  
/opt/jdk/jre/lib/amd64/libjfx*.so &&\  
sed -e "s|export PATH=|export PATH=/opt/jdk/bin:|" -i /etc/profile &&\  
curl -s https://letsencrypt.org/certs/lets-encrypt-x1-cross-signed.pem -o
/lets-encrypt-x1-cross-signed.pem &&\  
curl -s https://letsencrypt.org/certs/lets-encrypt-x2-cross-signed.pem -o
/lets-encrypt-x2-cross-signed.pem &&\  
curl -s https://letsencrypt.org/certs/lets-encrypt-x3-cross-signed.pem -o
/lets-encrypt-x3-cross-signed.pem &&\  
curl -s https://letsencrypt.org/certs/lets-encrypt-x4-cross-signed.pem -o
/lets-encrypt-x4-cross-signed.pem &&\  
/opt/jdk/bin/keytool -trustcacerts -keystore /opt/jdk/jre/lib/security/cacerts
-storepass changeit -noprompt -importcert -alias lets-encrypt-x1-cross-signed
-file /lets-encrypt-x1-cross-signed.pem &&\  
/opt/jdk/bin/keytool -trustcacerts -keystore /opt/jdk/jre/lib/security/cacerts
-storepass changeit -noprompt -importcert -alias lets-encrypt-x2-cross-signed
-file /lets-encrypt-x2-cross-signed.pem &&\  
/opt/jdk/bin/keytool -trustcacerts -keystore /opt/jdk/jre/lib/security/cacerts
-storepass changeit -noprompt -importcert -alias lets-encrypt-x3-cross-signed
-file /lets-encrypt-x3-cross-signed.pem &&\  
/opt/jdk/bin/keytool -trustcacerts -keystore /opt/jdk/jre/lib/security/cacerts
-storepass changeit -noprompt -importcert -alias lets-encrypt-x4-cross-signed
-file /lets-encrypt-x4-cross-signed.pem &&\  
rm -f /*.pem &&\  
chmod 500 /docker-entrypoint.sh &&\  
chmod -f 600 /etc/ssh.cache/ssh_host_* &&\  
mkdir -p ~root/.ssh &&\  
chmod 700 ~root/.ssh/ &&\  
echo -e "Port 22\n" >> /etc/ssh/sshd_config &&\  
cp -a /etc/ssh /etc/ssh.cache && \  
mkdir -p /var/run/sshd &&\  
addgroup -g 1000 jenkins &&\  
adduser -h /home/jenkins \  
-u 1000 \  
-G jenkins \  
-s /bin/ash \  
-D jenkins &&\  
echo "jenkins:jenkins" | chpasswd &&\  
mkdir -p ${JENKINS_HOME} &&\  
chown jenkins:jenkins ${JENKINS_HOME} &&\  
echo "jenkins ALL=(ALL) NOPASSWD: ALL" >>/etc/sudoers &&\  
echo "Installing aws-cli" &&\  
cd /tmp &&\  
curl -s https://s3.amazonaws.com/aws-cli/awscli-bundle.zip -o awscli-
bundle.zip &&\  
unzip awscli-bundle.zip &&\  
./awscli-bundle/install -i /usr/local/aws -b /usr/local/bin/aws &&\  
rm -rf awscli* &&\  
git config --global credential.helper '!/usr/local/bin/aws codecommit
credential-helper $@' &&\  
git config --global credential.useHttpPath true  
  
  
VOLUME ${JENKINS_HOME}  
  
EXPOSE 22/tcp  

