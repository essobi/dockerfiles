FROM gitlab/gitlab-runner  
  
ENV DEBIAN_FRONTEND noninteractive  
  
#Install ansible  
RUN apt-get update && apt-get -y dist-upgrade  
  
RUN apt-get update  
  
RUN apt-get install -y locales git sudo aptitude vim net-tools curl  
RUN apt-get install -y libffi-dev libssl-dev libyaml-dev  
RUN apt-get install -y python-crypto  
RUN apt-get install -y python python-dev  
RUN apt-get install -y python-pip  
  
RUN pip install --upgrade setuptools  
RUN pip install --upgrade PyYAML dnspython pyasn1 jinja2 paramiko ansible  
  
RUN mkdir /etc/ansible  
COPY ansible.cfg /etc/ansible/  
  
#Install docker  
RUN apt-get update &&\  
apt-get -y install apt-transport-https ca-certificates  
RUN apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys
58118E89F3A912897C070ADBF76221572C52609D  
RUN echo "deb https://apt.dockerproject.org/repo ubuntu-trusty
main">/etc/apt/sources.list.d/docker.list  
RUN apt-get update &&\  
apt-get -y install docker-engine  
  
#install expect so that we can emulate a terminal when running tests with
gitlab-ci  
RUN apt-get install -y expect-dev  
  
RUN apt-get install -y jq  

