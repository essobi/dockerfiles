FROM debian:jessie  
MAINTAINER Alan LaMielle <alan.lamielle+github@gmail.com>  
  
RUN apt-get update && \  
apt-get install -y s3cmd cron bzip2 ca-certificates && \  
rm -rf /var/lib/apt/lists/*  
  
ADD s3cfg /root/.s3cfg  
  
ADD start.sh /start.sh  
RUN chmod +x /start.sh  
  
ADD sync.sh /sync.sh  
RUN chmod +x /sync.sh  
  
ADD tar.sh /tar.sh  
RUN chmod +x /tar.sh  
  
ENTRYPOINT ["/start.sh"]  
CMD [""]  

