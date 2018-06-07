FROM debian:jessie  
MAINTAINER Christian Meter <meter@cs.uni-duesseldorf.de>  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV locs /etc/locale.gen  
  
# Install packages  
RUN apt-get update -qq && \  
apt-get install -yqq locales texlive-full python-pygments gnuplot inkscape git
openssh-client && \  
gem install rake  
  
# Create locales (needed to build latex files)  
RUN mv $locs $locs.bak && \  
touch $locs && \  
echo "de_DE.UTF-8 UTF-8" >> $locs && \  
echo "en_US.UTF-8 UTF-8" >> $locs && \  
locale-gen  
  
# Set language  
ENV LANG de_DE.UTF-8  
# Add ssh host key of our Gitlab Server  
RUN mkdir /root/.ssh && \  
ssh-keyscan -t rsa gitlab.cs.uni-duesseldorf.de >> /root/.ssh/known_hosts  

