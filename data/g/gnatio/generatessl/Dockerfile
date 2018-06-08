FROM m3adow/letsencrypt  
MAINTAINER Corey Butler  
  
ADD ./build /usr/bin/buildssl  
  
RUN chmod +x /usr/bin/buildssl  
  
ENTRYPOINT ["buildssl"]  

