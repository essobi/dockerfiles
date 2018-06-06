FROM alpine:3.5  
MAINTAINER Johannes Schickling "schickling.j@gmail.com"  
ENV SCHEDULE **None**  
ENV TIMEZONE America/Maceio  
  
ADD install.sh install.sh  
RUN sh install.sh && rm install.sh  
  
ADD run.sh run.sh  
ADD cleanup.sh cleanup.sh  
  
CMD ["sh", "run.sh"]  

