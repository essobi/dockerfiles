FROM ubuntu:12.04  
MAINTAINER Krzysztof Suszynski <krzysztof.suszynski@wavesoftware.pl>  
  
RUN apt-get update  
RUN apt-get install -y curl sudo python-software-properties  
RUN gpg --keyserver hkp://keys.gnupg.net --recv-keys
409B6B1796C275462A1703113804BB82D39DC0E3  
RUN \curl -sSL https://get.rvm.io | bash -s stable  
RUN bash -l -c 'rvm install 2.1'  
RUN bash -l -c 'rvm install 2.0'  
RUN bash -l -c 'rvm install 1.9'  
RUN bash -l -c 'rvm install 1.8'  
  
RUN bash -l -c 'rvm use 2.1 && gem install bundler'  
RUN bash -l -c 'rvm use 2.0 && gem install bundler'  
RUN bash -l -c 'rvm use 1.9 && gem install bundler'  
RUN bash -l -c 'rvm use 1.8 && gem install bundler'  
  
RUN useradd --create-home --shell /bin/bash travis  
RUN echo 'travis:travis' | chpasswd  
RUN usermod -aG sudo travis  
RUN usermod -aG rvm travis  
RUN echo '%sudo ALL=NOPASSWD: ALL' > /etc/sudoers.d/sudo-nopasswd  
RUN chmod 0440 /etc/sudoers.d/sudo-nopasswd  
  
ENTRYPOINT /bin/su - travis

