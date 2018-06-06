FROM mateuszm/carbon:1.0.2  
MAINTAINER mateuszmoneta@gmail.com  
  
ENV DESTINATIONS='127.0.0.1:2004'\  
USE_WHITELIST='False'\  
RELAY_METHOD='rules'  
EXPOSE 2013 2014  
ENTRYPOINT ["/carbon-entrypoint.py", "carbon-relay.py"]  

