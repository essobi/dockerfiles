# Stable version of etherpad doesn't support npm 2  
FROM tvelocity/etherpad-lite  
MAINTAINER Santiago Saavedra <ssaavedra@gpul.org>  
  
COPY entrypoint.sh /entrypoint.sh  
  
EXPOSE 9001  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["bin/run.sh", "--root"]  

