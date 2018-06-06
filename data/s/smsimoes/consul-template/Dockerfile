FROM smsimoes/clean-debian-image:latest  
LABEL maintainer="Miguel Simões <msimoes@gmail.com>"  
#  
# Ensure that the machine is always built with the most recent versions  
# and removing all non required artifacts to minimize the image size  
RUN DEBIAN_FRONTEND=noninteractive apt-get update -qqq  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -qq wget runit unzip -y  
RUN DEBIAN_FRONTEND=noninteractive apt-get upgrade -y -qq  
#  
# Add the external packages that are required to be installed  
RUN wget --quiet https://releases.hashicorp.com/consul-template/0.19.4/consul-
template_0.19.4_linux_amd64.zip -O /tmp/consul-template.zip  
RUN unzip /tmp/consul-template.zip -d /usr/local/bin  
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

