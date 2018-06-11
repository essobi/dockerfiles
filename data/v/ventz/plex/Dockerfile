FROM centos:6.8  
VOLUME ["/p"]  
  
COPY start-plex.sh /  
RUN yum install -y wget util-linux-ng  
RUN wget
https://raw.githubusercontent.com/mrworf/plexupdate/master/plexupdate.sh ; \  
chmod 755 plexupdate.sh && ./plexupdate.sh -p -a ; \  
rm -f plexmediaserver*  
  
EXPOSE 32400  
# Run actual Plex server  
CMD ["/start-plex.sh"]  

