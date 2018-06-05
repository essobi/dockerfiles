FROM area51/docker-client  
MAINTAINER Peter Mount <peter@retep.org>  
  
ENV JENKINS_HOME /opt/jenkins  
ENV JENKINS_PORT 80  
RUN apk add --no-cache \  
git \  
mercurial \  
subversion  
  
COPY keys/* /etc/ssh.cache/  
  
COPY scripts/*.sh /  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
RUN chmod 500 /docker-entrypoint.sh &&\  
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
mkdir ${JENKINS_HOME}s &&\  
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
  
COPY jenkins.war /opt/jenkins.war  
  
EXPOSE 22/tcp 80/tcp 443/tcp 50000/tcp  

