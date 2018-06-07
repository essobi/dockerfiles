FROM ubuntu:14.04  
MAINTAINER Thomas VIAL  
  
# Update and install packages  
RUN apt-get update  
RUN apt-get install -y curl zsh git vim  
RUN apt-get install -y -q php5-cli php5-curl  
RUN apt-get install parallel  
  
# Create "behat" user with password crypted "behat"  
RUN useradd -d /home/behat -m -s /bin/zsh behat  
RUN echo "behat:behat" | chpasswd  
RUN cd /home/behat && git clone
https://github.com/jaffamonkey/behat-3-kickstart.git  
  
# Behat alias in docker container  
# ADD behat /home/behat-3-kickstart/vendor/behat/behat/bin/behat  
# Create a new zsh configuration from the provided template  
ADD .zshrc /home/behat/.zshrc  
  
# Fix permissions  
RUN chown -R behat:behat /home/behat/behat-3-kickstart  
  
# Add "behat" to "sudoers"  
# RUN echo "behat ALL=(ALL:ALL) ALL" >> /etc/sudoers  
RUN echo "behat ALL=NOPASSWD: ALL" >> /etc/sudoers  
  
USER behat  
WORKDIR /home/behat/behat-3-kickstart  
ENV HOME /home/behat  
ENV PATH $PATH:/home/behat  
  
# Clone oh-my-zsh  
RUN git clone https://github.com/robbyrussell/oh-my-zsh.git /home/behat/.oh-
my-zsh/  
  
# Install Behat  
RUN cd /home/behat/behat-3-kickstart && curl http://getcomposer.org/installer
| php  
RUN cd /home/behat/behat-3-kickstart && php composer.phar install --prefer-
source  
RUN cd /home/behat/behat-3-kickstart && bin/behat -f pretty
features/api.feature

