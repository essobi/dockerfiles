FROM postgres  
LABEL maintainer="Mic Szillat <mic@nomaster.cc>"  
ADD backup.sh .  
ENV PGHOST=db  
ENV PGUSER=postgres  
ENV PGPASSWORD=postgres  
VOLUME /backup  
CMD ./backup.sh  

