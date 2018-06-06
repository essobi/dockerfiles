FROM scienceis/uoa-catchit-common:latest  
  
MAINTAINER ws@sit.auckland.ac.nz  
  
# Edit the following environment variable, commit to Github and it will
trigger Docker build  
# Since we fetch the latest changes from the associated Application~s master
branch  
# this helps trigger date based build  
ENV LAST_BUILD_DATE "Wed Apr 11 12:13:00 NZDT 2016"  
# copy over the app folder with data samples  
COPY app/* /srv/shiny-server/  
  
COPY shiny-server.sh /usr/bin/shiny-server.sh  
  
RUN chmod +x /usr/bin/shiny-server.sh && echo $LAST_BUILD_DATE > /srv/shiny-
server/build.txt  
  
CMD ["/usr/bin/shiny-server.sh"]  

