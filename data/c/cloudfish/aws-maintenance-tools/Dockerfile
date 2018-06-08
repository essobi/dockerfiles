FROM ubuntu:latest  
RUN apt-get -y update && apt-get -y upgrade  
  
# common  
RUN apt-get install -y wget git gcc make bzip2 unzip build-essential curl  
RUN apt-get install -y vim  
  
# direnv  
RUN wget -O direnv
https://github.com/direnv/direnv/releases/download/v2.13.1/direnv.linux-amd64  
RUN chmod +x direnv && mv direnv /usr/local/bin/ && echo 'eval "$(direnv hook
bash)"' >> ~/.bashrc  
  
# rbenv  
RUN apt-get install -y libssl-dev libreadline-dev zlib1g-dev  
RUN git clone git://github.com/sstephenson/rbenv.git .rbenv  
RUN git clone https://github.com/sstephenson/ruby-build.git
~/.rbenv/plugins/ruby-build  
RUN echo 'export PATH="$HOME/.rbenv/bin:$PATH"' >> ~/.bashrc && echo 'eval
"$(rbenv init -)"' >> ~/.bashrc  
ENV PATH="$HOME/.rbenv/bin:$PATH"  
RUN rbenv install 2.4.2 ; rbenv global 2.4.2  
RUN echo 'gem: --no-rdoc --no-ri' >> /.gemrc  
# piculet  
RUN ~/.rbenv/shims/gem install piculet  
# awspec  
RUN ~/.rbenv/shims/gem install awspec  
  
# awscli  
RUN apt-get install -y python-setuptools python2.7-dev  
RUN easy_install pip  
RUN pip install awscli  
RUN echo "complete -C '/usr/local/bin/aws_completer' aws" >> $HOME/.bashrc  
  
# ansible  
RUN pip install ansible  
  
# packer  
RUN mkdir ~/.packer && wget
https://releases.hashicorp.com/packer/1.1.2/packer_1.1.2_linux_amd64.zip &&
unzip packer_1.1.2_linux_amd64.zip && mv packer ~/.packer/  
RUN echo 'export PATH="$PATH:$HOME/.packer"' >> $HOME/.bashrc  
ENV USER root  
  
# yarn  
RUN apt-get -y install apt-transport-https nodejs npm  
RUN npm cache clean  
RUN npm install n -g  
RUN n stable  
RUN ln -sf /usr/local/bin/node /usr/bin/node  
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add -  
RUN echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee
/etc/apt/sources.list.d/yarn.list  
RUN apt-get update && apt-get -y install yarn  
  
# awslogs  
RUN pip install awslogs  
  
# exec  
CMD ["/bin/bash"]  

