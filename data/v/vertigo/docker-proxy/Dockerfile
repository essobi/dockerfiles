FROM vertigo/lets-nginx  
  
MAINTAINER Andre Fernandes <andre@vertigo.com.br>  
  
ARG BASEREPO  
ARG EPELREPO  
ENV DOCKERGID 999  
ADD src/docker-entrypoint.sh /docker-entrypoint.sh  
  
RUN chmod +x /docker-entrypoint.sh  
  
EXPOSE 80 443  
CMD ["/docker-entrypoint.sh"]  

