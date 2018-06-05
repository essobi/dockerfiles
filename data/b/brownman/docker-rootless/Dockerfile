FROM ubuntu:14.10  
MAINTAINER pgolm "golm.peter@gmail.com"  
# pgolm/docker-gitlab-ci-runner  
ENV DEBIAN_FRONTEND noninteractive  
  
# Config  
ENV INSTALL_RUBY_VERSION 2.1.0  
# apt-get deps  
RUN apt-get update -y  
RUN apt-get upgrade -y  
  
#RUN apt-get install -y -q  
RUN apt-get install -y curl libxml2-dev libxslt-dev libcurl4-openssl-dev
libreadline6-dev libssl-dev patch build-essential zlib1g-dev openssh-server
libyaml-dev libicu-dev \  
wget git build-essential libicu-dev \  
lsb-release software-properties-common tklib zlib1g-dev libssl-dev \  
libxml2 libxml2-dev libxslt1-dev  
# libreadline-gplv2-dev  
#The following packages have unmet dependencies:  
# libreadline-gplv2-dev : Conflicts: libreadline6-dev but 6.3-8ubuntu1 is to
be installed  
# libreadline6-dev : Conflicts: libreadline-gplv2-dev but 5.2+dfsg-2 is to be
installed  
#RUN add-apt-repository "deb http://archive.ubuntu.com/ubuntu $(lsb_release
-sc) main universe restricted multiverse"  
# switch priveleges  
RUN adduser --disabled-login --gecos 'GitLab CI Runner' gitlab_ci_runner  
USER gitlab_ci_runner  
ENV HOME /home/gitlab_ci_runner  
  
# install ruby, bundler  
RUN wget -qO - https://raw.github.com/fesplugas/rbenv-
installer/master/bin/rbenv-installer | bash  
ENV RBENV_ROOT ${HOME}/.rbenv  
ENV PATH ${RBENV_ROOT}/bin:${PATH}  
  
RUN rbenv install $INSTALL_RUBY_VERSION  
RUN rbenv global $INSTALL_RUBY_VERSION  
RUN echo "eval \"\$(rbenv init -)\"" >> $HOME/.profile  
RUN . $HOME/.profile && gem install bundler  
  
# install gitlab-ci-runner  
WORKDIR /home/gitlab_ci_runner  
RUN git clone https://github.com/gitlabhq/gitlab-ci-runner.git runner  
# Jan 02, 2014  
ENV RUNNER_REVISION 08f2260ae87e101f72194a27229b249d126e35fe  
RUN cd runner && git checkout $RUNNER_REVISION && . $HOME/.profile && bundle
install  
  
# prepare SSH  
RUN mkdir -p $HOME/.ssh  
  
CMD cd $HOME/runner  
CMD . ../.profile && ssh-keyscan -H $GITLAB_SERVER_FQDN >>
$HOME/.ssh/known_hosts && bundle exec ./bin/setup_and_run  

