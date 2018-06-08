FROM ubuntu:14.04  
MAINTAINER Sang-Hoon RHEE <akeymakr@mgail.com>  
  
RUN adduser --system --home /var/lib/munin --shell /bin/false \--uid 1103
--group munin  
  
RUN apt-get update -qq ; \  
env RUNLEVEL=1 DEBIAN_FRONTEND=noninteractive \  
apt-get install -y -qq cron munin heirloom-mailx libhttp-daemon-perl  
  
COPY dumb-init_1.0.1_amd64 /dumb-init  
RUN chmod +x /dumb-init  
  
COPY darkhttpd-1.12.from.git_amd64 /darkhttpd  
RUN chmod +x /darkhttpd  
  
COPY start.sh /  
COPY server.pl /  
COPY add-node.sh /  
COPY remove-node.sh /  
COPY test.sh /  
  
EXPOSE 8000  
VOLUME /var/lib/munin  
VOLUME /var/log/munin  
  
WORKDIR /var/lib/munin  
  
CMD [ "/dumb-init", "/start.sh" ]  

