FROM rabbitmq:3-management  
MAINTAINER DevOps <devops@actualsalesgroup.com>  
#  
# Ensure that the server has the correct timezone installed  
RUN ln -sf /usr/share/zoneinfo/UTC /etc/localtime  
#  
# Ensure that we have the latest packages associated with the image  
RUN DEBIAN_FRONTEND=noninteractive apt-get update -qq  
RUN DEBIAN_FRONTEND=noninteractive apt-get upgrade -y -qq  
#  
# Copy the autocluster plugins into the rabbitmq plugins folder and enable it  
COPY plugins/* /usr/lib/rabbitmq/lib/rabbitmq_server-3.6.14/plugins/  
RUN rabbitmq-plugins --offline enable autocluster  
RUN rabbitmq-plugins enable rabbitmq_stomp  
RUN rabbitmq-plugins enable rabbitmq_web_stomp  
#  
# Remove the packages that are no longer required after the package has been
installed  
RUN DEBIAN_FRONTEND=noninteractive apt-get autoremove --purge -q -y  
RUN DEBIAN_FRONTEND=noninteractive apt-get autoclean -y -q  
RUN DEBIAN_FRONTEND=noninteractive apt-get clean -y  
#  
# Remove all non-required information from the system to have the smallest  
# image size as possible  
RUN rm -rf /usr/share/doc/* /usr/share/man/?? /usr/share/man/??_*
/usr/share/locale/* /var/cache/debconf/*-old /var/lib/apt/lists/* /tmp/*  
#  
# Ensure that the port for the web stomp plugin is exposed on the server  
EXPOSE 15674  
#  
# And start the broker instance using the base command from the official image  
CMD ["rabbitmq-server"]  

