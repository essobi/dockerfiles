FROM rossbannerman/git:latest  
  
LABEL maintainer="Ross Bannerman <ross@bnnr.mn>"  
  
RUN apk add --no-cache curl  
  
RUN mkdir -p /etc/adblock/blocklists  
RUN git clone https://github.com/notracking/hosts-blocklists.git
/etc/adblock/blocklists  
  
COPY files/blocklist_updater /bin/blocklist_updater  
COPY files/root /var/spool/cron/crontabs/root  
  
RUN chmod +x /bin/blocklist_updater  
  
CMD crond -l 2 -f  

