FROM dingster94/java-centos-docker-slave:latest  
MAINTAINER Roger Ding  
  
ENV
PATH="/usr/local/rvm/gems/ruby-2.4.1/bin:/usr/local/rvm/gems/ruby-2.4.1@global/bin:/usr/local/rvm/rubies/ruby-2.4.1/bin:$PATH"  
ENV GEM_HOME="/usr/local/rvm/gems/ruby-2.4.1"  
ENV
GEM_PATH="/usr/local/rvm/gems/ruby-2.4.1:/usr/local/rvm/gems/ruby-2.4.1@global"  
COPY jenkins-slave /usr/local/bin/jenkins-slave  
  
USER root  
  
RUN yum groupinstall -y development && \  
yum install -y epel-release && \  
yum install -y readline-devel zlib-devel libffi-devel libyaml-devel openssl-
devel sqlite-devel && \  
yum install -y git && \  
yum install -y java && \  
yum install -y docker && \  
yum install -y which  
  
RUN curl -sSL https://rvm.io/mpapis.asc | gpg --import - && \  
curl -L get.rvm.io | bash -s stable  
  
RUN bash -c "source /etc/profile.d/rvm.sh && rvm reload && rvm requirements
run && rvm install 2.4 && rvm use 2.4 --default && echo 'source
/etc/profile.d/rvm.sh' >> ~/.profile;"  
  
ENTRYPOINT ["jenkins-slave"]  

