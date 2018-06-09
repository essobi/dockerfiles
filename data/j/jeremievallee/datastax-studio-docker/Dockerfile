FROM java:8  
MAINTAINER Jeremie Vallee <jeremie.vallee@gmail.com>  
  
RUN apt-get update  
  
# Get DataStax Studio  
WORKDIR /opt  
ADD https://downloads.datastax.com/datastax-studio/datastax-
studio-1.0.0.tar.gz /opt/  
RUN tar -xzvf datastax-studio-1.0.0.tar.gz -C .  
RUN rm datastax-studio-1.0.0.tar.gz  
RUN mkdir /var/lib/datastax-studio  
  
# Configure DataStax Studio  
RUN sed -i "s/ httpBindAddress: localhost/ httpBindAddress: 0.0.0.0/"
/opt/datastax-studio-1.0.0/conf/configuration.yaml  
RUN sed -i "s/ baseDirectory: null/ baseDirectory: \/var\/lib\/datastax-
studio/" /opt/datastax-studio-1.0.0/conf/configuration.yaml  
  
WORKDIR /  
  
VOLUME [ "/var/lib/datastax-studio" ]  
  
# Expose DataStax Studio Port  
EXPOSE 9091  
ENTRYPOINT ["/opt/datastax-studio-1.0.0/bin/server.sh"]  

