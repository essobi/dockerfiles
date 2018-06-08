FROM gitlab/gitlab-runner  
  
#Install ansible  
RUN DEBIAN_FRONTEND=noninteractive apt-get update && apt-get -y dist-upgrade  
  
RUN DEBIAN_FRONTEND=noninteractive apt-get update && \  
apt-get install -y locales python-pip python-dev \  
git sudo aptitude vim \  
libffi-dev libssl-dev curl \  
net-tools  
RUN pip install --upgrade PyYAML jinja2 paramiko ansible dnspython setuptools
pyasn1  
RUN mkdir /etc/ansible  
COPY ansible.cfg /etc/ansible/  
  
#Install docker  
RUN DEBIAN_FRONTEND=noninteractive apt-get update &&\  
apt-get -y install apt-transport-https ca-certificates  
RUN apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys
58118E89F3A912897C070ADBF76221572C52609D  
RUN echo "deb https://apt.dockerproject.org/repo ubuntu-trusty
main">/etc/apt/sources.list.d/docker.list  
RUN apt-get update &&\  
apt-get -y install docker-engine  
  
#Docker in docker  
RUN set -x &&\  
addgroup --system dockremap &&\  
adduser --system --group dockremap &&\  
echo 'dockremap:165536:65536' >> /etc/subuid &&\  
echo 'dockremap:165536:65536' >> /etc/subgid  
  
ENV DIND_COMMIT 3b5fac462d21ca164b3778647420016315289034  
  
RUN wget
"https://raw.githubusercontent.com/docker/docker/${DIND_COMMIT}/hack/dind" -O
/usr/local/bin/dind \  
&& chmod +x /usr/local/bin/dind  
  
VOLUME /var/lib/docker  
EXPOSE 2375  
#install expect so that we can emulate a terminal when running tests with
gitlab-ci  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y expect-dev  
  
RUN addgroup gitlab-runner docker  
COPY docker_gitlab-ci_entrypoint /  
RUN chmod +x /docker_gitlab-ci_entrypoint  
  
ENTRYPOINT ["/docker_gitlab-ci_entrypoint"]  
CMD ["run", "--user=gitlab-runner", "--working-directory=/home/gitlab-runner"]  

