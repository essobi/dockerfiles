FROM linuxkonsult/chef-solo  
  
MAINTAINER Tom Eklöf tom@linux-konsult.com  
  
# Expose the SMTP/SSH port  
EXPOSE 25  
EXPOSE 22  
ENV LANG C.UTF-8  
# Add chef files  
ADD ./solo.rb /etc/chef/solo.rb  
ADD ./node.json /etc/chef/node.json  
# Add Berksfile to install cookbooks  
ADD ./Berksfile /Berksfile  
ADD ./install_cmds.sh /install_cmds.sh  
# Add daily crontab  
ADD ./cron.daily /etc/  
  
# Run cookbooks  
RUN /install_cmds.sh  
  
# Add supervisord services  
ADD ./supervisor /etc/supervisor  
  
# Start the service  
CMD ["/usr/bin/supervisord", "--nodaemon"]  

