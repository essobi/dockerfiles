############################################################  
# Dockerfile that creates a container for running Foreman (nightly) on
phusion/baseimage  
# (which is just a modified version of Ubuntu)  
#  
# Recommended build command:  
#  
# docker build -t foreman /path/to/Dockerfile/dir/.  
#  
# Recommended run command:  
#  
# docker run -t --hostname="foreman.company.com" --name=foreman -p 8443:443 -p
8080:80 foreman  
#  
# That will expose Foreman on ports 8443 and 8080 with the given hostname (use
your own).  
############################################################  
FROM raseel/ubuntu-trusty  
MAINTAINER Raseel Bhagat <raseelbhagat@gmail.com>  
  
# Ensures apt doesn't ask us silly questions:  
ENV DEBIAN_FRONTEND noninteractive  
  
# Install Puppet  
RUN apt-get -y install ca-certificates  
RUN wget https://apt.puppetlabs.com/puppetlabs-release-pc1-trusty.deb && \  
dpkg -i puppetlabs-release-pc1-trusty.deb  
  
# Add the Foreman repos  
RUN echo "deb http://deb.theforeman.org/ trusty 1.13" >
/etc/apt/sources.list.d/foreman.list && \  
echo "deb http://deb.theforeman.org/ plugins 1.13" >>
/etc/apt/sources.list.d/foreman.list  
RUN apt-get -y install ca-certificates && \  
wget -q https://deb.theforeman.org/pubkey.gpg -O- | apt-key add -  
RUN apt-get update && apt-get -y install foreman-installer  
  
# Copy our first_run.sh script into the container:  
# COPY first_run.sh /usr/local/bin/first_run.sh  
# RUN chmod 755 /usr/local/bin/first_run.sh  
# Also copy our installer script  
# COPY install_foreman.sh /opt/install_foreman.sh  
# RUN chmod 755 /opt/install_foreman.sh  
# Perform the installation  
# RUN bash /opt/install_foreman.sh  
# RUN rm -f /opt/install_foreman.sh # Don't need it anymore  
# Expose our HTTP/HTTPS ports:  
EXPOSE 80  
EXPOSE 443  
# Our 'first run' script which takes care of resetting the DB the first time  
# the image runs with subsequent runs being left alone:  
# CMD ["/usr/local/bin/first_run.sh"]  
CMD ["/usr/sbin/foreman-installer", "--verbose"]  

