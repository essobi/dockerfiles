FROM ioarchitectjp/otrs5_helpdesk_jp:latest  
MAINTAINER Tomohisa Hirami<hirami@io-architect.com>  
  
COPY instpkg.sh inst.sh mysql_init.sh /  
RUN chmod 775 /inst.sh /instpkg.sh /mysql_init.sh ; sync; /inst.sh  

