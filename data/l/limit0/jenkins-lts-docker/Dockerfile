FROM jenkins/jenkins:lts  
USER root  
RUN curl -sSL https://get.docker.com/ | sh  
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - && \  
echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee
/etc/apt/sources.list.d/yarn.list && \  
apt-get update && \  
apt-get install -y yarn && \  
rm -rf /var/lib/apt/lists/*  
RUN usermod -aG docker jenkins  
USER jenkins  

