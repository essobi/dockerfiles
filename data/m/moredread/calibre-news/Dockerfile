FROM quay.io/moredread/calibre:latest  
MAINTAINER code@andre-bubel.de  
  
USER root  
  
RUN apt-get update && apt-get install python3 -y  
RUN mkdir /news  
ADD fetch_news.sh /news  
ADD call_every_week.py /news  
RUN chown user:user /news -R  
  
USER user  
  
CMD ["python3", "-u", "/news/call_every_week.py", "/news/fetch_news.sh"]  

