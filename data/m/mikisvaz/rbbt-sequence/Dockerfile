FROM mikisvaz/rbbt-basic  
ADD allowed_biomart_archives /home/rbbt/.rbbt/etc/allowed_biomart_archives  
USER root  
ADD provision.sh /tmp/provision.sh  
RUN /bin/bash /tmp/provision.sh  
USER rbbt  

