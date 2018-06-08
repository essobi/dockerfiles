FROM ubuntu:14.04  
MAINTAINER nayuta "https://github.com/nayuta"  
# Create default user  
RUN useradd -m -s /bin/bash ubuntu  
RUN chown -R ubuntu:ubuntu /home/ubuntu  
  
# Add addable locale  
RUN locale-gen $(grep '\\.UTF-8' /usr/share/i18n/SUPPORTED | awk '{ print $1
}')  
RUN update-locale en_US.UTF-8  
  
# Set default locale  
SET LC_ALL=en_US.UTF-8  
SET LANG=en_US.UTF-8  
# Install packages for building ruby  
RUN apt-get update  
RUN apt-get install -y build-essential curl git  
RUN apt-get install -y zlib1g-dev libssl-dev libreadline-dev libyaml-dev
libxml2-dev libxslt-dev  
RUN apt-get install -y gawk libsqlite3-dev sqlite3 autoconf libgdbm-dev
libncurses5-dev automake libtool bison pkg-config libffi-dev  
RUN apt-get clean  
  
# Install rvm  
RUN sudo -u ubuntu -H bash -l -c "\curl -sSL https://get.rvm.io | bash -s
stable"  
  
# Install multiple versions of ruby  
Add rubyversions.txt /home/ubuntu/.rubyversions  
ENV CONFIGURE_OPTS --disable-install-doc  
RUN chown ubuntu:ubuntu /home/ubuntu/.rubyversions  
RUN sudo -u ubuntu -H bash -l -c "rvm autolibs 2"  
RUN sudo -u ubuntu -H bash -l -c "xargs -L 1 rvm install <
/home/ubuntu/.rubyversions"  
  
# Gem setting for root/ubuntu  
RUN echo 'gem: --no-rdoc --no-ri' >> /home/ubuntu/.gemrc  
  
# Install Bundler for each version of ruby  
RUN sudo -u ubuntu -H bash -l -c 'for v in $(cat /home/ubuntu/.rubyversions);
do rvm use --default $v; gem install bundle; done'  
  
# Install Default Gemfile  
#ADD ./Gemfile /root/Gemfile  
#RUN bash -l -c 'cd /root/; for v in $(cat rubies.txt); do rvm use --default
$v; bundle install; done'  

