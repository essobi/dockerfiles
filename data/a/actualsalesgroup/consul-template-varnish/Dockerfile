FROM actualsalesgroup/consul-template:latest  
MAINTAINER Miguel Simões <miguel.simoes@actualsalesgroup.com>  
#  
# Ensure that we have the latest packages associated with the image  
RUN DEBIAN_FRONTEND=noninteractive apt-get update -qq  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y -qq varnish  
RUN DEBIAN_FRONTEND=noninteractive apt-get upgrade -y -qq  
#  
# Remove the packages that are no longer required after the package has been
installed  
RUN DEBIAN_FRONTEND=noninteractive apt-get autoremove --purge -q -y  
RUN DEBIAN_FRONTEND=noninteractive apt-get autoclean -y -q  
RUN DEBIAN_FRONTEND=noninteractive apt-get clean -y  
#  
# Add the configuration required for the cache server  
ADD conf/varnish.vcl /etc/varnish/default.vcl  
#  
# Add the required service configuration to runit and ensure they  
# have execution permissions associated  
ADD services/varnish.service /etc/service/varnish/run  
#  
# Remove all non-required information from the system to have the smallest  
# image size as possible  
RUN rm -rf /usr/share/doc/* /usr/share/man/?? /usr/share/man/??_*
/usr/share/locale/* /var/cache/debconf/*-old /var/lib/apt/lists/* /tmp/*  
#  
# And we start the container...  
CMD ["/usr/bin/runsvdir", "/etc/service"]  
  

