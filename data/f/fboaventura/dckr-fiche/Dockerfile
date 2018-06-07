FROM busybox  
  
LABEL maintainer "Frederico Freire Boaventura <frederico@boaventura.net>"  
LABEL version "1.0"  
  
ENV DOMAIN "localhost"  
ENV SLUG 8  
ENV BUFFER 4096  
ENV USER "root"  
ENV PORT "9999"  
ADD files/fiche-static /fiche  
ADD files/index.html /data/  
  
EXPOSE 9999  
VOLUME /data  
  
CMD /fiche -d ${DOMAIN} -o /data -l /dev/stdout -p ${PORT} -s ${SLUG} -B
${BUFFER} -u ${USER}  

