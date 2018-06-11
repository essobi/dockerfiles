  
#FROM cruize_base  
FROM vera/cruize_base:latest  
  
MAINTAINER "Daniel Vera" vera@genomics.fsu.edu  
VOLUME /gbdb  
VOLUME /usr/local/bin  
  
ENV CGI_BIN=/var/www/cgi-bin  
ENV SAMTABIXDIR=/opt/samtabix/  
ENV USE_SSL=1  
ENV USE_SAMTABIX=1  
ENV MACHTYPE=x86_64  
ENV
PATH=/root/bin/x86_64:/opt/samtabix/:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin  
  
RUN yum update -y && yum install -y \  
mariadb.x86_64  
  
RUN echo -e '#!/usr/bin/env bash\nif [[ ! $(ls -A /usr/local/bin) ]]; then git
clone https://github.com/fsugenomics/cruize_scripts /usr/local/bin; fi ;
update_browser' > /usr/bin/start && chmod +x /usr/bin/start  
  
CMD ["start"]  

