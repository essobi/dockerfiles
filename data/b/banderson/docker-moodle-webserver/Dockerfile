FROM williamyeh/ansible:debian8  
  
MAINTAINER brendan_anderson@hcpss.org  
  
LABEL vendor=Howard\ County\ Public\ Schools \  
org.hcpss.version="1.0.0" \  
org.hcpss.name="moodle_webserver"  
  
ADD ansible /srv/provisioning  
  
# Run the provisioning playbook.  
RUN ansible-galaxy install -r /srv/provisioning/requirements.yml \  
&& ansible-playbook /srv/provisioning/provision.yml -v -c local  
  
# Remove ansible and provisioning locations, which may contain secrets  
RUN rm -rf /srv/provisioning  
  
COPY apache2-foreground /usr/local/bin/  
COPY docker-entrypoint.sh /entrypoint.sh  
  
# It makes sense to me to define the web root as a volume at this time as we  
# have just installed the webserver which makes this directory significant.  
# However, doing so makes the directory unusable for derived docker images as  
# any further changes to it would be reverted to the state it was in when it
was  
# first declaired a volume.  
#  
# There is some debate over whether this behavior is a feature or a bug:  
#  
# https://github.com/docker/docker/issues/3639  
# VOLUME ["/var/www"]  
ENTRYPOINT ["/entrypoint.sh"]  
  
EXPOSE 80 443  
CMD ["apache2-foreground"]  

