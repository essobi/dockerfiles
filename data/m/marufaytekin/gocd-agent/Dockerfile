###########################################################  
# Build using: docker build -t gocd-agent .  
# based on official gocd/gocd-agent latest image.  
# installs:  
# docker engine to enable docker in docker  
# maven, ant, and nodejs for builds  
# ruby, capybara, and cucumber requirements to run automated tests.  
###########################################################  
FROM gocd/gocd-agent:latest  
  
MAINTAINER marufaytekin  
  
  
###########################################################  
# install docker engine to use docker client # from the agent.  
# In order to use docker client make sure you give r/w  
# prmissions to /var/run/docker.sock file on the docker host.  
###########################################################  
RUN touch /etc/apt/sources.list.d/docker.list \  
&& echo "deb https://apt.dockerproject.org/repo ubuntu-trusty main"
>>/etc/apt/sources.list.d/docker.list \  
&& apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys
58118E89F3A912897C070ADBF76221572C52609D \  
&& apt-get update \  
&& apt-get install -y --force-yes docker-engine \  
&& usermod -aG docker go  
  
  
###########################################################  
# installs maven and ant.  
###########################################################  
RUN apt-get install -y --force-yes maven  
  
  
###########################################################  
# install nodejs  
###########################################################  
RUN echo "go ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers \  
&& su - go -c "touch ~/.bashrc" \  
&& su - go -c "curl -o-
https://raw.githubusercontent.com/creationix/nvm/v0.31.0/install.sh | bash" \  
&& su - go -c ". ~/.nvm/nvm.sh && nvm install 5.9.0" \  
&& su - go -c "touch ~/.npmrc" \  
&& su - go -c "echo strict-ssl=false >> ~/.npmrc" \  
&& su - go -c "echo config="strict-ssl=false" >> ~/.npmrc" \  
&& su - go -c "echo minTimeout=300000 >> ~/.npmrc" \  
  
  
###########################################################  
# install ruby, capybara, and cucumber.  
###########################################################  
  
# give go user sudo rights  
RUN echo "go ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers  
  
# install requirements.  
RUN apt-add-repository ppa:brightbox/ruby-ng \  
&& apt-get update  
RUN apt-get install -y --force-yes software-properties-common  
RUN apt-get install -y --force-yes build-essential  
RUN apt-get install -y --force-yes zlib1g-dev  
RUN apt-get install -y --force-yes ruby1.9.3  
RUN apt-get install -y --force-yes firefox  
RUN apt-get install -y --force-yes xvfb  
  
RUN gem install bundler  
ADD Gemfile /var/go  
RUN su - go -c "bundle install"  

