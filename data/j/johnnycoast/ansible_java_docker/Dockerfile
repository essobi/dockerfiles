FROM ubuntu:xenial  
  
ARG DEBIAN_FRONTEND=noninteractive  
  
RUN echo "===> Installing Ansible..." && \  
apt-get update -y && apt-get install --fix-missing && \  
apt-get install -y software-properties-common && \  
apt-add-repository ppa:ansible/ansible && \  
apt-get update && \  
apt-get install -y ansible  
  
RUN echo "===> Installing Java 8..." && \  
apt-get update -y && \  
apt-get install -y software-properties-common && \  
apt-add-repository ppa:webupd8team/java && \  
apt-get update -y && \  
apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 \--recv-keys EEA14886 &&
\  
echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true |
/usr/bin/debconf-set-selections && \  
apt-get install -y oracle-java8-installer && \  
apt-get install -y oracle-java8-unlimited-jce-policy && \  
apt-get clean  
  
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle  
  
ADD ./ansible/ /var/ansible  
  
RUN ansible-playbook /var/ansible/provision-docker.yml -i
/var/ansible/inventory/inventory-docker  
  
CMD [ "ansible-playbook", "--version" ]  

