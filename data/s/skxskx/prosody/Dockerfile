#  
# Build it:  
# sudo docker build -t skxskx/prosody .  
#  
# Then launch it:  
# sudo docker run -d -p 5222:5222 skxskx/prosody  
#  
# NOTE: There is no local-storage setup.  
#  
FROM ubuntu  
MAINTAINER steve@steve.org.uk  
ENV DEBIAN_FRONTEND noninteractive  
  
#  
# ensure our sources are up-to-date  
#  
RUN apt-get update  
  
#  
# Install the software.  
#  
RUN apt-get install --yes --force-yes lua5.1 prosody  
  
#  
# Disable deamonization, so the server stays in the foreground.  
#  
RUN perl -pi -e "s/daemonize = true;/daemonize = false;/g"
/etc/prosody/prosody.cfg.lua  
  
#  
# Allow account registration  
#  
RUN perl -pi -e "s/allow_registration = false;/allow_registration = true;/g"
/etc/prosody/prosody.cfg.lua  
  
#  
# Setup dummy certts  
#  
RUN ln -s /etc/prosody/certs/localhost.key /etc/prosody/certs/example.com.key  
RUN ln -s /etc/prosody/certs/localhost.cert /etc/prosody/certs/example.com.crt  
  
#  
# Now set some configuration up.  
#  
# This is an example which configures "chat.example.com"  
#  
RUN echo "VirtualHost \"chat.example.com\"" >
/etc/prosody/conf.d/example.cfg.lua  
RUN echo Component \"rooms.chat.example.com\" \"muc\" >>
/etc/prosody/conf.d/example.cfg.lua  
RUN echo "restrict_room_creation = false" >>
/etc/prosody/conf.d/example.cfg.lua  
  
#  
# Make a PIDfile directory  
#  
RUN mkdir -p /var/run/prosody  
RUN chown prosody.prosody /var/run/prosody  
  
#  
# Expose the port  
#  
EXPOSE 5222  
#  
# Set the user we'll run as.  
#  
USER prosody  
  
#  
# Now launch the startup-command  
#  
CMD [ "/usr/bin/lua5.1", "/usr/bin/prosody" ]  
  

