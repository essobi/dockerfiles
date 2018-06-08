FROM ubuntu:14.04  
MAINTAINER ohtake<manabu.ohtake.297@gmail.com>  
  
RUN apt-get install -y software-properties-common  
RUN apt-add-repository ppa:ansible/ansible  
RUN apt-get update -y  
RUN apt-get install -y ansible wget git curl openssl libreadline6-dev
libreadline6 libxml2-dev libxslt-dev libyaml-dev libssl-dev build-essential
python-pip jq  
  
RUN git clone https://github.com/sstephenson/rbenv.git /root/.rbenv  
RUN git clone https://github.com/sstephenson/ruby-build.git
/root/.rbenv/plugins/ruby-build  
RUN /root/.rbenv/plugins/ruby-build/install.sh  
ENV PATH /root/.rbenv/bin:$PATH  
RUN echo 'eval "$(rbenv init -)"' >> /etc/profile.d/rbenv.sh # or /etc/profile  
RUN echo 'eval "$(rbenv init -)"' >> .bashrc  
  
# Install multiple versions of ruby  
ENV CONFIGURE_OPTS --disable-install-doc  
ADD ./versions.txt /root/versions.txt  
RUN xargs -L 1 rbenv install < /root/versions.txt  
  
# Install Bundler for each version of ruby  
RUN echo 'gem: --no-rdoc --no-ri' >> /.gemrc  
RUN bash -l -c 'for v in $(cat /root/versions.txt); do rbenv global $v; gem
install bundler; done'  
RUN wget https://dl.bintray.com/mitchellh/vagrant/vagrant_1.7.2_x86_64.deb &&
dpkg -i vagrant_1.7.2_x86_64.deb  
RUN bash -l -c 'gem install bundler serverspec specinfra'  
RUN bash -l -c 'vagrant plugin install vagrant-aws'  
RUN bash -l -c 'pip install awscli'  

