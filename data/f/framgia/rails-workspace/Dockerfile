FROM phusion/passenger-full:0.9.19  
# Install "software-properties-common" (for the "add-apt-repository")  
RUN apt-get update && apt-get install -y \  
software-properties-common \  
supervisor  
  
# Install Gems  
COPY gems /tmp/gems  
RUN cd /tmp/gems && bundle install  
  
RUN rm /etc/nginx/sites-enabled/default  
  
ADD env.conf /etc/nginx/main.d/env.conf  
  
ADD webapp.conf /etc/nginx/sites-enabled/webapp.conf  
  
RUN apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \  
rm -f /etc/service/nginx/down  
  
COPY entrypoint.sh /scripts/entrypoint.sh  
RUN chmod a+x /scripts/entrypoint.sh  
  
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
EXPOSE 80 443 3000  
WORKDIR /home/app  
  
ENV HOME /root  
  
ENTRYPOINT ["/scripts/entrypoint.sh"]  
CMD ["/sbin/my_init"]  

