FROM actualsalesgroup/cleaned-docker-image:latest  
MAINTAINER devops@actualsalesgroup.com  
#  
# Ensure that we have the latest packages associated with the image  
RUN DEBIAN_FRONTEND=noninteractive apt-get update -qq  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -qq wget runit unzip -y  
RUN DEBIAN_FRONTEND=noninteractive apt-get upgrade -y -qq  
#  
# Add the external packages that are required to be installed  
RUN wget --quiet https://releases.hashicorp.com/consul-template/0.16.0/consul-
template_0.16.0_linux_amd64.zip -O /tmp/consul-template.zip  
RUN unzip /tmp/consul-template.zip -d /usr/local/bin  
#  
# Add consul-cli interface binary  
ADD bin/consul-cli /usr/local/bin/consul-cli  
RUN chmod a+x /usr/local/bin/consul-cli  
#  
# Remove the packages that are no longer required after the package has been
installed  
RUN DEBIAN_FRONTEND=noninteractive apt-get purge wget unzip -y -q  
RUN DEBIAN_FRONTEND=noninteractive apt-get autoremove --purge -q -y  
RUN DEBIAN_FRONTEND=noninteractive apt-get autoclean -y -q  
RUN DEBIAN_FRONTEND=noninteractive apt-get clean -y  
#  
# Remove all non-required information from the system to have the smallest  
# image size as possible  
RUN rm -rf /usr/share/doc/* /usr/share/man/?? /usr/share/man/??_*
/usr/share/locale/* /var/cache/debconf/*-old /var/lib/apt/lists/* /tmp/*  
#  
# And we start the container...  
CMD ["/usr/bin/runsvdir", "/etc/service"]  

