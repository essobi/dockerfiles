#  
# Base Hyperdex Dockerfile  
# Adds the hyperdex list and updates  
#  
FROM colinrhodes/base  
  
MAINTAINER Colin Rhodes <colin@colin-rhodes.com>  
  
ADD http://ubuntu.hyperdex.org/hyperdex.gpg.key hyperdex.key  
RUN apt-key add hyperdex.key  
RUN rm hyperdex.key  
ADD http://ubuntu.hyperdex.org/trusty.list
/etc/apt/sources.list.d/hyperdex.list  
RUN apt-get -yq update  
RUN apt-get -yq install libbusybee2 libe1 libreplicant1  

