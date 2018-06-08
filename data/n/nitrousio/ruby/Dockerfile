FROM nitrousio/nodejs:latest  
MAINTAINER Nitrous.IO <hello@nitrous.io>  
  
RUN \  
mkdir -p /usr/local/opt/rbenv && \  
/bin/bash -c 'chown -R $NITROUS_USERNAME:$NITROUS_USERNAME
/usr/local/opt/rbenv'  
  
RUN \  
echo 'export RBENV_ROOT=/usr/local/opt/rbenv' >> /etc/profile && \  
echo 'export PATH=$RBENV_ROOT/bin:$PATH' >> /etc/profile && \  
echo 'eval "$($RBENV_ROOT/bin/rbenv init -)"' >> /etc/profile && \  
echo 'export PATH=.bundle/binstubs:$PATH' >> /etc/profile  
  
COPY files/.gemrc /home/$NITROUS_USERNAME/.gemrc  
COPY files/bundle-config /home/$NITROUS_USERNAME/.bundle/config  
  
RUN \  
/bin/bash -c 'chown -R $NITROUS_USERNAME:$NITROUS_USERNAME
/home/nitrous/.gemrc /home/nitrous/.bundle'  
  
USER $NITROUS_USERNAME  
  
RUN \  
/bin/bash -c \  
'git clone https://github.com/sstephenson/rbenv.git /usr/local/opt/rbenv && \  
git clone https://github.com/sstephenson/ruby-build.git
/usr/local/opt/rbenv/plugins/ruby-build'  
  
RUN \  
/bin/bash -l -c \  
'rbenv install 2.1.5 && \  
rbenv global 2.1.5 && \  
gem install bundler --version=1.7.9'  
  
USER root  

