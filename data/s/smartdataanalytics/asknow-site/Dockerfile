FROM whitegecko/dockerjekyllpages  
MAINTAINER Gezim Sejdiu <g.sejdiu@gmail.com>  
  
ADD run.sh /run.sh  
RUN chmod a+x /run.sh  
  
VOLUME /data/jekyll/source  
  
EXPOSE 80  
CMD ["/run.sh"]

