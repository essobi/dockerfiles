#  
# Create an image with Puppet 4.x agent within  
#  
# Could be used with foreman as well as raw puppet master  
#  
# @author : Michel CHA  
FROM debian  
  
WORKDIR /root  
  
#ENV VARNAME value  
# Shell form to run command -> will interpret variable defined with ENV  
# RUN execute the command in a new layer -> recommended for tool installation  
# Multiple RUN is possible  
# Avoid the use of ADD => unpredictable  
# Update packages  
RUN apt-get update \  
&& apt-get -y install wget inotify-tools vim locales ntp locate  
  
# Compile locales  
COPY resources/etc/locale.gen /etc/locale.gen  
RUN locale-gen en_US.utf8 && locale-gen fr_FR.utf8  
  
# Setup NTP  
COPY resources/etc/ntp.conf /etc/ntp.conf  
RUN service ntp restart  
  
# Install Puppet Agent  
RUN apt-get -y install ca-certificates \  
&& wget https://apt.puppetlabs.com/puppetlabs-release-pc1-jessie.deb \  
&& dpkg -i puppetlabs-release-pc1-jessie.deb \  
&& apt-get update \  
&& apt-get -y install puppet-agent  
RUN rm -f puppetlabs-release-pc1-jessie.deb  
COPY resources/etc/default /etc/default  
COPY resources/etc/puppetlabs/puppet /etc/puppetlabs/puppet/  
  
# Stick Puppet version  
COPY resources/etc/apt/preferences.d /etc/apt/preferences.d  
COPY resources/stick_puppet_version.sh stick_puppet_version.sh  
RUN chmod u+x stick_puppet_version.sh  
RUN /root/stick_puppet_version.sh  
  
# Setup to be finished inside running container  
COPY resources/setup_cert.sh setup_cert.sh  
COPY resources/services.sh services.sh  
COPY resources/start.sh start.sh  
  
RUN chmod u+x setup_cert.sh services.sh start.sh  
  
# Other resources  
COPY resources/.bashrc .bashrc  
  
# Exec form to run command -> will not interpret variable defined with ENV  
# Exec form is recommanded for CMD and ENTRYPOINT  
# CMD is used to specify a default command to run (only one CMD per
Dockerfile)  
CMD ["/root/start.sh"]  
  
# When CMD is mixed with ENTRYPOINT  
# Then CMD's value provide the args to the command in ENTRYPOINT  
# This ensure a parameterized ENTRYPOINT  
# Ex : docker run image_alias yyy  
# will result in xxx yyy  
#ENTRYPOINT ["xxx"]  

