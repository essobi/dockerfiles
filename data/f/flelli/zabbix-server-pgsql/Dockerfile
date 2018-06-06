FROM zabbix/zabbix-server-pgsql:alpine-latest  
  
# Copy the custom alert script and make it accessible and executable  
#
------------------------------------------------------------------------------  
# Update: the following lines won't work because the destination file is in a  
# directory that has been declared as an external volume in parent images.  
# According to Docker docs
(https://docs.docker.com/engine/reference/builder/#notes-about-specifying-
volumes),  
# "If any build steps change the data within the volume after it has been
declared, those changes will be discarded."  
# So the only way is to mount a host volume containing the file when the
container is created.  
#
------------------------------------------------------------------------------  
#ADD https://github.com/flelli/slack-integrations/raw/master/slack-zabbix-
alert.sh /usr/lib/zabbix/alertscripts/  
#RUN chown 100:1000 /usr/lib/zabbix/alertscripts/slack-zabbix-alert.sh &&
chmod 755 /usr/lib/zabbix/alertscripts/slack-zabbix-alert.sh  
RUN apk add \--no-cache curl curl-dev libcurl  

