FROM jenkins:2.60.2  
MAINTAINER Raphael P. Ribeiro  
  
USER root  
RUN apt-get update \  
&& apt-get install -y curl git build-essential default-libmysqlclient-dev
libxml2-dev sudo \  
gawk libreadline6-dev libssl-dev libyaml-dev libsqlite3-dev sqlite3 autoconf \  
libgmp-dev libgdbm-dev libncurses5-dev automake libtool bison pkg-config
libffi-dev \  
imagemagick libqt4-dev libqtwebkit-dev xvfb libfontconfig-dev libjpeg-dev  
  
# ruby gems dependencies  
RUN apt-get install -y libpq-dev libqt4-dev postgresql  
  
# java building  
RUN apt-get install -y maven  
  
# docker inside docker  
RUN groupadd -g 118 docker  
RUN usermod -a -G docker jenkins  
RUN echo "jenkins ALL=NOPASSWD: ALL" >> /etc/sudoers  
  
#RUN curl -sSL https://rvm.io/mpapis.asc | gpg --import - \  
#&& \curl -sSL https://get.rvm.io | bash -s -- --autolibs=enable --ruby=2.2.5
--gems=bundler  
#RUN adduser jenkins rvm  
# install RVM, Ruby, and Bundler  
RUN gpg --keyserver hkp://keys.gnupg.net --recv-keys
409B6B1796C275462A1703113804BB82D39DC0E3
7D2BAF1CF37B13E2069D6956105BD0E739499BDB  
RUN \curl -sSL https://get.rvm.io | sed -E
s/\\_rvm\\_print\\_headline/\\_rvm\\_version/ | bash -s stable
--autolibs=enable \--ruby=2.2.5  
RUN /bin/bash -l -c "rvm --default use ruby-2.2.5"  
RUN /bin/bash -l -c "rvm @global do gem install bundler"  
RUN usermod -a -G rvm,docker jenkins  
#RUN /bin/bash -l -c "echo 'source /etc/profile.d/rvm.sh' >>
$JENKINS_HOME/.bashrc"  
USER jenkins  

