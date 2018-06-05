FROM area51/docker-client  
MAINTAINER Peter Mount <peter@retep.org>  
  
ENV JENKINS_HOME /home/jenkins  
  
RUN apk add --update \  
git \  
mercurial \  
subversion &&\  
rm -rf /var/cache/apk/*  
  
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
mkdir -p ${JENKINS_HOME} &&\  
chown jenkins:jenkins ${JENKINS_HOME}  
  
VOLUME ${JENKINS_HOME}  
  
RUN addgroup -g 1001 cloud &&\  
adduser -h /home/cloud \  
-u 1001 \  
-G cloud \  
-s /bin/ash \  
-D cloud &&\  
echo "cloud:jenkins.password" | chpasswd &&\  
mkdir -p /home/cloud &&\  
chown cloud:cloud /home/cloud  
  
RUN (echo "jenkins ALL=(ALL) NOPASSWD: ALL"; echo "cloud ALL=(ALL) NOPASSWD:
ALL") >>/etc/sudoers  
  
EXPOSE 22/tcp  
  

