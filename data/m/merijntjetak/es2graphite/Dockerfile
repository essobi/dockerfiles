FROM gliderlabs/alpine  
  
RUN apk --update add bash python py-pip  
RUN pip install requests==2.5.1  
  
ADD es2graphite.py /es2graphite.py  
RUN chmod a+x /es2graphite.py  
  
ADD docker-entrypoint.sh /docker-entrypoint.sh  
RUN chmod a+x /docker-entrypoint.sh  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  

