FROM busybox:1.27.2  
# Default Execution Time (7:27:14 AM, staggered to minimize load on
nameserver)  
ENV exec_hour=7 \  
exec_min=27 \  
exec_sec=14  
# Copy cron script  
COPY cronscript.sh /usr/bin/cronscript  
  
# Add Script to Cron Job  
RUN mkdir -p /var/spool/cron/crontabs && \  
echo -e "${exec_min} ${exec_hour} * * * /bin/sleep ${exec_sec} ; /bin/sh
/usr/bin/cronscript\n" \  
>> /var/spool/cron/crontabs/www-data  
  
CMD ["crond", "-f"]  

