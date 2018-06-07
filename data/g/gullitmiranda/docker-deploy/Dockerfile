# The container includes Nginx + Passenger on top of 'gullitmiranda/ruby':  
#  
# * Ubuntu 14.04  
# * Git  
# * MRI Ruby 2.1.2  
# * Bundler  
# * Foreman  
#  
# Adds:  
#  
# * Passenger  
# * Nginx  
# * Git bare  
#  
FROM gullitmiranda/ruby  
MAINTAINER Gullit Miranda "https://github.com/gullitmiranda"  
# Setup Ruby  
RUN apt-get update -qq && apt-get upgrade -y -qq > /dev/null  
  
#
==============================================================================  
# Phusion Passenger, Nginx version  
#
==============================================================================  
ENV PASSENGER_VERSION 4.0.53  
# Install passenger  
RUN /bin/bash -l -c \  
'gem install passenger --version $PASSENGER_VERSION'  
  
# Install passenger-nginx  
RUN /bin/bash -l -c \  
'passenger-install-nginx-module --auto-download --auto --prefix=/opt/nginx'  
  
#
==============================================================================  
# Git post-receive  
#
==============================================================================  
# Install openssh-server  
RUN apt-get install -y openssh-server  
  
RUN mkdir -m 0755 /var/run/sshd  
  
ENV PROJECT ""  
ENV PUBLIC_KEY ""  
ENV USER git  
ENV PROVISION ""  
ENV PROVISION_PATH ""  
RUN sed -ri 's/#?RSAAuthentication\s+.*/RSAAuthentication yes/'
/etc/ssh/sshd_config  
RUN sed -ri 's/#?PasswordAuthentication\s+.*/PasswordAuthentication no/'
/etc/ssh/sshd_config  
RUN sed -ri 's/#?PermitEmptyPasswords\s+.*/PermitEmptyPasswords no/'
/etc/ssh/sshd_config  
RUN sed -ri 's/#?PubkeyAuthentication\s+.*/PubkeyAuthentication yes/'
/etc/ssh/sshd_config  
RUN sed -ri 's/#?UseLogin\s+.*/UseLogin no/' /etc/ssh/sshd_config  
RUN sed -ri 's/#?LogLevel\s+.*/LogLevel INFO/' /etc/ssh/sshd_config  
RUN sed -ri 's/#?UsePAM\s+.*/UsePAM yes/g' /etc/ssh/sshd_config  
  
# Clean up APT and temporary files when done  
RUN apt-get clean -qq && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Define working directory.  
# WORKDIR $GIT_DIR  
# Expose port for Passenger  
EXPOSE 443  
# expose port for ssh  
EXPOSE 22  
ADD https://raw.githubusercontent.com/gullitmiranda/docker-
deploy/master/run.sh /run.sh  
RUN chmod +x /run.sh  
  
CMD ["/run.sh"]  

