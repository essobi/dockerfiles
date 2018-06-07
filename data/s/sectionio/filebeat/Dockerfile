FROM scratch  
LABEL maintainer "section.io <support@section.io>"  
  
VOLUME /etc/filebeat /var/lib/filebeat /var/log  
WORKDIR /etc/filebeat  
  
ADD "filebeat-5.4.0-linux-x86_64.tar.gz" /  
ENTRYPOINT ["/filebeat-5.4.0-linux-x86_64/filebeat"]  

