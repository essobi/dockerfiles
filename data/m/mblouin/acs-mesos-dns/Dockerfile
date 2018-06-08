FROM mrbobbytables/mesos-dns  
MAINTAINER Michael Blouin <contact@michaelblouin.ca>  
  
ENV MESOSDNS_AUTOCONF "disabled"  
ENV MESOSDNS_CONF /config.json  
  
EXPOSE 53  
COPY config.json /config.json  
  
CMD ["mesos-dns", "-config=/config.json"]  

