FROM sqz88/shiny-base  
  
COPY shiny-server.conf /etc/shiny-server/shiny-server.conf  
COPY shiny-server.sh /usr/bin/shiny-server.sh  
RUN chmod +x /usr/bin/shiny-server.sh  
  
RUN rm -rf /srv/shiny-server/index.html /srv/shiny-server/sample-apps  
ADD ./app/fune/ /srv/shiny-server/  
  
CMD ["/usr/bin/shiny-server.sh"]

