FROM debian:stretch-slim  
  
RUN mkdir /data  
  
ADD rdf.tgz /data  
ADD gitty.tgz /data  
ADD toe.tgz /data  
COPY passwd /data  
  
RUN useradd vre4eic_data  
RUN chown -R vre4eic_data.vre4eic_data /data && \  
chown -R root /data/config-enabled && \  
chmod -R ug+rwX /data/data  

