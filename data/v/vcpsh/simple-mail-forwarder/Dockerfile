FROM zixia/simple-mail-forwarder  
MAINTAINER AK Internet <internet@vcp.sh>  
RUN echo "sender_canonical_maps = regexp:/etc/postfix/sender_canonical_maps"
>> /etc/postfix/main.cf  
RUN echo "/.+/ catchall@vcp.sh" >> /etc/postfix/sender_canonical_maps  

