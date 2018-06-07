FROM eclipse/stack-base:ubuntu  
  
ENV RVM_VERSION 1.29.1  
ENV RUBY_VERSION 2.4.1  
ENV RAILS_VERSION 5.1.1  
ENV GEM_VERSION 2.6.12  
ENV BUNDLER_VERSION 1.15.1  
ENV RAKE_VERSION 12.0.0  
USER root  
  
RUN echo 'gem: --no-rdoc --no-ri ' >> /etc/gemrc  
  
USER user  
RUN sudo apt-get update && sudo apt-get install -y nodejs mysql-client
postgresql-client sqlite3 libpq-dev vim curl --no-install-recommends && sudo
rm -rf /var/lib/apt/lists/*  
  
RUN gpg --keyserver hkp://keys.gnupg.net --recv-keys
409B6B1796C275462A1703113804BB82D39DC0E3 \  
&& curl -sSL https://get.rvm.io | /bin/bash -s -- --version $RVM_VERSION \  
&& echo "source /home/user/.rvm/scripts/rvm" >> /home/user/.bashrc  
  
RUN /bin/bash -l -c "source /home/user/.rvm/scripts/rvm \  
&& rvm install $RUBY_VERSION \--autolibs=enable \  
&& rvm use $RUBY_VERSION \--default \  
&& rvm $RUBY_VERSION do gem update --system $GEM_VERSION \  
&& rvm $RUBY_VERSION do gem install rails -v $RAILS_VERSION \  
&& rvm $RUBY_VERSION do gem install bundler -v $BUNDLER_VERSION \  
&& rvm $RUBY_VERSION do gem install rake -v $RAKE_VERSION"  
  
EXPOSE 3000  

