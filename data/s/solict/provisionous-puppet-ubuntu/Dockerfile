###############################################################################  
# Provisionous Docker/Puppet profile  
# OS: Ubuntu 12.04 (trusty)  
# Equivalent: Debian 8 (jessie)  
###############################################################################  
FROM ubuntu:trusty  
MAINTAINER Luís Pedro Algarvio <lp.algarvio@gmail.com>  
  
# Configure the enviroment  
ENV TERM linux  
RUN export DEBIAN_FRONTEND="noninteractive";  
WORKDIR /root  
  
# Configure Apt  
RUN echo "APT::Install-Recommends "\""false"\"";" >> /etc/apt/apt.conf;  
RUN echo "APT::Install-Suggests "\""false"\"";" >> /etc/apt/apt.conf;  
  
# Clear and Update the Apt cache if it is outdated  
RUN ["/bin/bash", "-c", "if [ \  
\"$(stat -c %Y /var/lib/apt/lists/partial)\" -lt \  
\"$(date +\"%s\" -d \"-3 days\")\" ]; \  
then apt-get clean all; apt-get update; \  
else echo \"Apt caches are up-to-date.\"; fi;"]  
  
# Install system dependencies  
RUN apt-get -qqy install apt-utils dialog bash-completion wget nano;  
  
# Configure /root profile  
RUN cp -R /etc/skel/. /root;  
  
# Upgrade the Apt packages  
RUN apt-get -qqy upgrade;  
  
# Install Ruby 1.9.3  
RUN apt-get -qqy install ruby1.9.3 ruby1.9.1-dev rubygems-integration;  
  
# Configure Rubygems  
RUN echo "gem: --no-ri --no-rdoc" > ~/.gemrc;  
  
# Install Puppet  
RUN apt-get -qqy install puppet;  
  
# Install system dependencies  
RUN apt-get -qqy install make gcc;  
  
# Install Librarian for Puppet  
RUN gem install librarian-puppet;  
  

