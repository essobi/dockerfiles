FROM alpine  
  
ENV \  
AUTOSSH_GATETIME=30 \  
AUTOSSH_POLL=10 \  
AUTOSSH_FIRST_POLL=30 \  
AUTOSSH_LOGLEVEL=1  
  
ADD /entrypoint.sh /entrypoint.sh  
RUN chmod 755 /entrypoint.sh \  
&& apk add \--no-cache autossh  
  
ENTRYPOINT ["/entrypoint.sh"]

