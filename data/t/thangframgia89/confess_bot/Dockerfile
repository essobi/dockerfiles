FROM phusion/passenger-full:0.9.19  
# Install "software-properties-common" (for the "add-apt-repository")  
RUN apt-get update && apt-get install -y \  
software-properties-common  
  
# Install Gems  
RUN cd /home/app && git clone https://github.com/ngocthang/confess_bot.git  
  
RUN ls -alh /home/app  
  
RUN rm /etc/nginx/sites-enabled/default  
  
ADD webapp.conf /etc/nginx/sites-enabled/webapp.conf  
  
RUN apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \  
rm -f /etc/service/nginx/down  
  
COPY entrypoint.sh /scripts/entrypoint.sh  
RUN chmod a+x /scripts/entrypoint.sh  
  
EXPOSE 80 3000  
WORKDIR /home/app  
  
ENTRYPOINT ["/scripts/entrypoint.sh"]  
CMD ["/sbin/my_init"]  

