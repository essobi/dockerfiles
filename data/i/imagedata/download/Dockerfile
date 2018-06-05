FROM centos:centos7  
MAINTAINER ome-devel@lists.openmicroscopy.org.uk  
  
RUN useradd data  
USER data  
  
# No https, so verify sha1  
RUN true \  
&& curl http://download.asperasoft.com/download/sw/connect/3.7.2/aspera-
connect-3.7.2.141527-linux-64.sh > /tmp/aspera.sh \  
&& test $(sha1sum /tmp/aspera.sh |cut -f1 -d\ ) =
66f8db1324d5c421be16f30602c637dfdb626480 \  
&& sh /tmp/aspera.sh \  
&& rm /tmp/aspera.sh  
  
ENV ASCP_KEY /home/data/.aspera/connect/etc/asperaweb_id_dsa.openssh  
ENV ASCP_LIMIT 40m  
ENV ASCP_PORT 33001  
ENV ASCP_SERVER fasp-beta.ebi.ac.uk  
ADD ascp.sh /usr/local/bin/ascp.sh  
ENTRYPOINT ["/usr/local/bin/ascp.sh"]  

