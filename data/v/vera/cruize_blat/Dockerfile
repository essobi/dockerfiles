  
#FROM cruize_base  
FROM vera/cruize_base:latest  
  
MAINTAINER "Daniel Vera" vera@genomics.fsu.edu  
  
VOLUME /gbdb  
VOLUME /usr/local/bin  
  
EXPOSE 80  
EXPOSE 443  
ENV CGI_BIN=/var/www/cgi-bin  
ENV SAMTABIXDIR=/opt/samtabix/  
ENV USE_SSL=1  
ENV USE_SAMTABIX=1  
ENV MACHTYPE=x86_64  
ENV
PATH=/root/bin/x86_64:/opt/samtabix/:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin  
  
RUN cd /opt/kent/src && make blatSuite  
  
RUN echo "if [[ ! $(ls -A /usr/local/bin) ]]; then git clone
https://github.com/fsugenomics/cruize_scripts /usr/local/bin; fi ;
update_blat" > /usr/bin/update && chmod +x /usr/bin/update  
  
CMD ["update"]  

