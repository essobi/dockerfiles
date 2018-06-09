FROM ubuntu:latest  
  
MAINTAINER Roberto Jimenez Sanchez, <jszroberto@gmail.com>  
  
RUN apt-get update && apt-get install wget apt-utils unzip jq git curl vim
nano -y  
  
#RUN apt-get install rubygems-integration -y  
# Installation of latest Ruby  
RUN gpg --keyserver hkp://keys.gnupg.net --recv-keys
409B6B1796C275462A1703113804BB82D39DC0E3  
RUN \curl -L https://get.rvm.io | bash -s stable --ruby  
RUN echo 'source /etc/profile.d/rvm.sh' >> ~/.bashrc  
  
# Install package dependencies  
RUN /usr/local/rvm/bin/rvm requirements  
  
# Install ruby  
RUN echo "gem: --no-rdoc --no-ri" >> ~/.gemrc  
#RUN /usr/local/rvm/bin/rvm install ruby --latest  
RUN /usr/local/rvm/bin/rvm install ruby install ruby 2.1.6  
  
# Installation of Bosh CLI  
RUN /bin/bash -l -c "gem install bundler --no-ri --no-rdoc"  
#RUN /bin/bash -l -c "gem cleanup bosh_cli"  
#RUN /bin/bash -l -c "bundle update bosh_cli"  
RUN /bin/bash -l -c "gem install bosh_cli --no-ri --no-rdoc -v 1.2652.0"  
#RUN /bin/bash -l -c "gem install bosh_cli bosh_cli_plugin_micro --no-ri --no-
rdoc"  
ENV ENV_CONFIG /workspace/env.conf  
VOLUME /workspace  
WORKDIR /workspace  
  
RUN mkdir /root/bin  
RUN echo 'export PATH=$PATH:/root/bin' >> ~/.bashrc  
RUN echo 'export PATH=$PATH:/root/bin' >> /etc/profile  
  
ADD bin/* /root/bin/  
RUN chmod +x /root/bin/*  
  
ENTRYPOINT bash -l -c "load.env run_ctl"  
CMD "bash"  

