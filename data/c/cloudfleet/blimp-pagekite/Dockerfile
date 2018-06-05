FROM ubuntu:14.04  
RUN echo "deb http://pagekite.net/pk/deb/ pagekite main" >
/etc/apt/sources.list.d/pagekite_net_pk_deb.list  
RUN apt-key adv --recv-keys --keyserver keys.gnupg.net AED248B1C7B2CAC3  
  
RUN apt-get update -y  
RUN apt-get install -y pagekite  
  
RUN rm /etc/pagekite.d/20_frontends.rc  
  
# pagekite.net service  
CMD pagekite --clean \  
\--defaults \  
\--service_on=https:blimp.$CLOUDFLEET_DOMAIN:nginx:443:$CLOUDFLEET_SECRET \  
\--service_on=http:blimp.$CLOUDFLEET_DOMAIN:nginx:80:$CLOUDFLEET_SECRET  
  
# our pagekite server  
# CMD pagekite --clean \  
# --frontend=$CLOUDFLEET_HOST \  
#
--service_on=http,https:blimp.$CLOUDFLEET_DOMAIN:nginx:443:$CLOUDFLEET_SECRET  

