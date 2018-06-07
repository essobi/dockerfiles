FROM jetty:9.3.10  
MAINTAINER michal@rovnanik.sk  
  
# install VIM  
RUN apt-get update  
RUN apt-get install vim -y  
RUN apt-get clean  
  
# copy XFORWPROTO xml into config folder  
COPY jetty-xforwproto.xml /usr/local/jetty/etc  

