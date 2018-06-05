# beli/firefox-flash  
FROM beli/firefox  
MAINTAINER Michal Belica <devel@beli.sk>  
USER root  
# enable multiverse repo  
RUN sed -ie 's/^\\(deb.* universe\\)[[:space:]]*$/\1 multiverse/'
/etc/apt/sources.list  
RUN apt-get update && apt-get install -y flashplugin-installer && apt-get
clean  
USER user  

