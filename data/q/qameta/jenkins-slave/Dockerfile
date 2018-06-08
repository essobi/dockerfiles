FROM qameta/jenkins-slave:base  
  
RUN \  
apt-get update && \  
apt-get install -y --no-install-recommends curl && \  
curl -sSL https://get.rvm.io | sudo bash -s stable --ruby  
  
# Setup locale  
RUN \  
echo "en_US UTF-8" > /etc/locale.gen && \  
locale-gen en_US.UTF-8 && \  
echo "export LC_ALL=en_US.UTF-8" >> ${JENKINS_HOME}/.bashrc && \  
echo "export LANGUAGE=en_US:en" >> ${JENKINS_HOME}/.bashrc && \  
echo "export LANG=en_US.UTF-8" >> ${JENKINS_HOME}/.bashrc  
  
RUN usermod -a -G rvm jenkins  
  
RUN /usr/local/rvm/bin/rvm alias create ruby ruby  
RUN echo "export PATH=/usr/local/rvm/rubies/ruby/bin:$PATH" >>
/home/jenkins/.bashrc

