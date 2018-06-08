FROM jenkins  
USER root  
RUN gpg --keyserver hkp://keys.gnupg.net --recv-keys
409B6B1796C275462A1703113804BB82D39DC0E3  
  
RUN /bin/bash -l -c "curl -L get.rvm.io | bash -s stable"  
RUN /bin/bash -l -c "rvm requirements"  
RUN /bin/bash -l -c "rvm install 2.3.1"  
RUN /bin/bash -l -c "echo 'gem: --no-ri --no-rdoc' > ~/.gemrc"  
RUN /bin/bash -l -c "gem install bundler --no-ri --no-rdoc"  
  
RUN apt-get install -y --no-install-recommends \  
postgresql-client \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN usermod -a -G rvm jenkins  
USER jenkins  

