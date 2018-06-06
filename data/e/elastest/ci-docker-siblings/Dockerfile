########################  
#  
# Docker file to explain docker in docker build run and test  
# a maven aplication  
#  
########################  
FROM ubuntu:16.04  
MAINTAINER Guiomar Tuñon <gtunon@naevatec.com>  
  
# user for setting the environment  
USER root  
  
# prepare environment  
RUN apt-get update && \  
apt-get install -y software-properties-common && \  
add-apt-repository ppa:webupd8team/java  
  
RUN apt-get update && \  
apt-get upgrade -y && \  
apt-get install -y curl wget apt-transport-https  
  
## java  
RUN echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select
true | debconf-set-selections && \  
apt-get install -y oracle-java8-installer && \  
rm -rf /var/lib/apt/lists/* && \  
rm -rf /var/cache/oracle-jdk8-installer  
  
# Define commonly used JAVA_HOME variable  
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle  
  
## maven  
RUN wget
http://mirrors.viethosting.vn/apache/maven/maven-3/3.3.9/binaries/apache-
maven-3.3.9-bin.tar.gz && \  
tar -xf apache-maven-3.3.9-bin.tar.gz -C /usr/local  
  
RUN ln -s /usr/local/apache-maven-3.3.9 /usr/local/maven  
  
ENV M2_HOME /usr/local/maven  
ENV PATH=${M2_HOME}/bin:${PATH}  
  
## docker  
RUN curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add -  
  
RUN add-apt-repository \  
"deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs)
stable"  
  
RUN apt-get update && \  
apt-get install -y docker-ce=17.06.0~ce-0~ubuntu  
# docker siblings (instead of docker in docker)  
RUN echo "export DOCKER_HOST='unix:///var/run/docker.sock'" >> /root/.bashrc \  
&& echo "export DEBIAN_FRONTEND=noninteractive" >> /root/.bashrc  
  
## aws cli  
# AWS CLI needs the PYTHONIOENCODING environment varialbe to handle UTF-8
correctly:  
ENV PYTHONIOENCODING=UTF-8  
# man and less are needed to view 'aws <command> help'  
# vim is useful to write shell scripts  
# python* is needed to install aws cli using pip install  
RUN apt-get install -y \  
less \  
man \  
python \  
python-pip \  
python-virtualenv \  
unzip \  
vim  
  
#RUN pip install awscli  
RUN curl "https://s3.amazonaws.com/aws-cli/awscli-bundle.zip" -o "awscli-
bundle.zip" && \  
unzip awscli-bundle.zip && \  
./awscli-bundle/install -i /var/lib/aws -b /usr/bin/aws  
  
## git  
RUN apt-get -y install git  
  
## netcat  
RUN apt-get -y install netcat  
  
## gpg2  
RUN apt-get -y install gnupg2  
  
#non root user  
RUN useradd -ms /bin/bash jenkins &&\  
echo "jenkins:jenkins" | chpasswd  
  
RUN usermod -aG docker jenkins  
  
# set envs  
ENV WORKSPACE /home/jenkins  
  
USER jenkins  
  
WORKDIR ${WORKSPACE}  
  
# launch container  
#ENTRYPOINT [ "/bin/bash" , "-c" , "./scripts/sh_entry_point.sh ${*}" ]  
ENTRYPOINT ["/bin/bash"]  

