FROM ubuntu:14.04  
MAINTAINER koichiro "https://github.com/sumyapp"  
# Update first  
RUN apt-get update -y  
RUN apt-get dist-upgrade -y  
  
# Create default user  
RUN useradd -m -s /bin/bash ubuntu  
RUN chown -R ubuntu:ubuntu /home/ubuntu  
  
# Add addable locale  
RUN locale-gen $(grep '\\.UTF-8' /usr/share/i18n/SUPPORTED | awk '{ print $1
}')  
RUN update-locale en_US.UTF-8  
  
# Set default locale  
RUN export LC_ALL=en_US.UTF-8  
RUN export LANG=en_US.UTF-8  
  
# Add language packs  
RUN apt-get install -y language-pack-ja  
  
# Install necessary packages  
RUN apt-get install -y build-essential  
RUN apt-get install -y git  
RUN apt-get install -y libssl-dev  
RUN apt-get install -y libxml2-dev libxslt-dev  
RUN apt-get install -y curl zip unzip  
# Install necessary packages(rbenv install 2.2.0)  
RUN apt-get install -y libffi-dev  
RUN apt-get install -y libreadline-dev  
  
# Install and setup ssh  
RUN apt-get install -y ssh  
RUN mkdir -p /var/run/sshd 2> /dev/null  
# Ignore host fingerprint check  
RUN sudo -u ubuntu -H bash -l -c 'mkdir /home/ubuntu/.ssh'  
RUN sudo -u ubuntu -H bash -l -c 'chmod 700 /home/ubuntu/.ssh'  
RUN sudo -u ubuntu -H bash -l -c 'echo "StrictHostKeyChecking no" >
/home/ubuntu/.ssh/config'  
RUN sudo -u ubuntu -H bash -l -c 'chmod 600 /home/ubuntu/.ssh/config'  
  
# Clean cache  
RUN apt-get clean  
  
# Check out rbenv  
RUN sudo -u ubuntu -H bash -l -c "git clone
https://github.com/sstephenson/rbenv.git ~/.rbenv"  
  
# Check out ruby-build  
RUN sudo -u ubuntu -H bash -l -c "git clone
https://github.com/sstephenson/ruby-build.git ~/.rbenv/plugins/ruby-build"  
  
# Create .bash_profile and set default locale on .bash_profile(with-rbenv)  
ADD dot_bash_profile /home/ubuntu/.bash_profile  
RUN chown ubuntu:ubuntu /home/ubuntu/.bash_profile  
  
# rbenv PATH changes take effect  
RUN sudo -u ubuntu -H bash -l -c "source ~/.bash_profile"  
RUN sudo -u ubuntu -H bash -l -c "rbenv --version"  
  
# Gem setting(--no-rdoc, --no-ri are deperecated, but it will work correctly)  
RUN echo 'gem: --no-rdoc --no-ri' >> /home/ubuntu/.gemrc  
  
# Install ruby  
RUN sudo -u ubuntu -H bash -l -c "rbenv install 2.2.0"  
  
# Set default ruby version  
RUN sudo -u ubuntu -H bash -l -c "rbenv global 2.2.0"  
  
# Install scss-lint from https://rubygems.org/gems/scss_lint  
RUN sudo -u ubuntu -H bash -l -c 'gem install scss_lint -v 0.41.0'  

