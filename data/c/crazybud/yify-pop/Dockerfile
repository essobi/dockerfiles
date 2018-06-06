# Select the latest ubuntu image to build this container  
########################################################  
FROM crazybud/base-ubu-latest:latest  
MAINTAINER crazyBUD  
  
# Add needed packages  
#####################  
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -yq git
nodejs npm  
  
# Yify-pop setup  
################  
  
RUN git clone https://github.com/yify-pop/yify-pop.git  
WORKDIR /yify-pop  
RUN npm -g install geddy && npm -g install geddy && npm -g install peerflix &&
npm install && ln -s /usr/bin/nodejs /usr/bin/node  
  
# Add conf file for `supervisor`  
################################  
  
ADD https://raw.githubusercontent.com/40thoughts/docker-Yify-
Pop/master/.apps.conf /etc/supervisor/conf.d/yify-pop.conf  
  
# Lighten the image if possible  
###############################  
RUN apt-get purge npm git -qy && apt-get autoremove -qy && apt-get clean all
&& rm -rf /tmp/*  
  
# Expose ports  
##############  
  
# expose port for http : 4000  
# "EXPOSE 4000"  
  
# expose port for streams (n ports = n streams)  
# e.g. "EXPOSE 8889 8890 8891 8892" allows 4 different movies/TV shows to be
streamed at the same time  
# "EXPOSE 8889 8890 8891 8892"  
  
EXPOSE 4000 8889 8890 8891 8892  
  
# Run `supervisor`  
##################  
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor.conf", "-n"]  

