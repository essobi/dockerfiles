###########################################################  
# Build using: docker build -f Dockerfile.cucumber -t gocd-agent .  
# based on official gocd/gocd-agent latest image.  
# installs:  
# docker engine to enable docker in docker  
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

