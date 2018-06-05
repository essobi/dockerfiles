FROM mwaeckerlin/letsencrypt  
MAINTAINER mwaeckerlin  
  
RUN apt-get update  
RUN apt-get install -y bind9  
  
EXPOSE 53  
ENV TTL "3600"  
ENV SERIAL ""  
ENV REFRESH "3600"  
ENV RETRY "1800"  
ENV EXPIRE "604800"  
ENV NEGATIVE_CACHE_TTL "1800"  
ENV DEFAULT_IP ""  
ENV DEFAULT_SUBDOMAINS "www"  
ENV DEFAULT_DOMAINS ""  
ENV TRANSFER ""  
ADD start.sh /start.sh  
ENTRYPOINT ["/bin/bash", "-c"]  
CMD ["/start.sh"]  

