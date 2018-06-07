FROM fvigotti/env-fatubuntu-bashsupervisor  
  
ENV TERM xterm  
  
RUN apt-get update && \  
apt-get install -y supervisor && \  
apt-get clean  
  
ADD config /config  
  
RUN chmod -R +x /config  

