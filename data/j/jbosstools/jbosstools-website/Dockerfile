FROM centos:centos7  
MAINTAINER Max Rydahl Andersen <max@jboss.org>  
  
# install deps required by our build  
RUN yum install -y epel-release which tar bzip2 gcc ruby-devel libxml2
libxml2-devel libxslt libxslt-devel libcurl-devel git  
  
# when running with above nodejs was not available  
RUN curl --silent --location https://rpm.nodesource.com/setup_6.x | bash -  
RUN yum install -y nodejs  
  
RUN yum install -y wget  
  
# Add RVM keys  
RUN gpg2 --keyserver hkp://keys.gnupg.net --recv-keys D39DC0E3  
  
# Install RVM  
RUN curl -L get.rvm.io | bash -s stable  
RUN /bin/bash -l -c "rvm requirements && rvm autolibs enable"  
  
# Install Ruby and its gems  
#ADD ./.ruby-version /tmp/  
ADD ./.ruby-gemset /tmp/  
ADD ./Gemfile /tmp/  
ADD ./Gemfile.lock /tmp/  
ADD ./Rakefile /tmp/  
  
WORKDIR /tmp/  
# tell rvm to install ruby instead of complaining it is missing.  
RUN /bin/bash -l -c "echo rvm_install_on_use_flag=1 > ~/.rvmrc"  
# rvm will get version from Gemfile  
RUN /bin/bash -l -c "rvm install ."  
RUN /bin/bash -l -c "gem install bundler"  
# install base gem's, if any changes user only need to install differences.  
RUN /bin/bash -l -c "bundle install"  
  
# Enable GPG support  
VOLUME /gnupg  
ENV GNUPGHOME /gnupg  
RUN touch /tmp/gpg-agent.conf  
RUN echo 'export GPG_TTY=$(tty); eval $(gpg-agent --daemon --no-use-standard-
socket --options /tmp/gpg-agent.conf );' >> ~/.bash_profile  
  
# Add the volume for the actual project  
VOLUME /jbosstools-website  
WORKDIR /jbosstools-website  
  
# Prevent encoding errors  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US.UTF-8  
ENV LC_ALL en_US.UTF-8  
EXPOSE 4242  
ENTRYPOINT [ "/bin/bash", "-l", "-c" ]  
CMD [ "rake", "clean", "preview" ]  
  

