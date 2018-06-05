FROM mateuszm/carbon:1.0.2  
MAINTAINER mateuszmoneta@gmail.com  
  
ENV DESTINATIONS='127.0.0.1:2004'\  
USE_WHITELIST='False'  
EXPOSE 2023 2024  
COPY aggregation.conf /etc/carbon/aggregation-rules.conf  
  
ENTRYPOINT ["/carbon-entrypoint.py", "carbon-aggregator.py"]  

