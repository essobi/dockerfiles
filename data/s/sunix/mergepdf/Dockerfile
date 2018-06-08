FROM ubuntu  
  
MAINTAINER Sun Seng David Tan <sunix@sunix.org>  
  
RUN apt-get update && \  
apt-get install -y ghostscript pdftk && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
RUN mkdir /data && chmod 777 /data  
  
CMD cd /data && pdftk *.pdf cat output large.pdf && pdf2ps large.pdf
very_large.ps && ps2pdf very_large.ps final.pdf && rm large.pdf very_large.ps  

