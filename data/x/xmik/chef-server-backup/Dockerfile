FROM ruby:2.2.3-slim  
MAINTAINER Ewa Czechowska <ewa@ai-traders.com>  
  
RUN mkdir /scripts  
COPY scripts /scripts  
ENV DEBIAN_FRONTEND=noninteractive  
  
# install knife-backup  
RUN apt-get update && \  
apt-get install -y build-essential && \  
cd /scripts && bundle install && \  
mkdir /root/.chef && mkdir -p /var/backups/chef-server && \  
mv /scripts/run_knife_backup.sh /usr/bin/run_knife_backup.sh && \  
chmod 755 /usr/bin/run_knife_backup.sh  
  
# clean  
RUN apt-get purge -y build-essential && \  
apt-get clean && \  
rm -rf /tmp/* /var/tmp/* && \  
rm -rf /var/lib/apt/lists/*  
# do not remove /scripts, there are Gemfiles to be used on each start up  
# add image metadata  
RUN touch /etc/docker_metadata.txt && \  
VERSION=$(cat /scripts/version.txt) && \  
echo -e "base_image_name = ruby\n\  
base_image_tag = 2.2.3-slim\n\  
this_image_name = xmik/chef-server-backup\n\  
this_image_tag = ${VERSION}\n\  
" >> /etc/docker_metadata.txt  
  
ENTRYPOINT ["/bin/bash", "-c"]  
CMD ["/usr/bin/run_knife_backup.sh"]

