FROM python:3.5  
MAINTAINER MASASHI MORITA <morita@mrita-it-lab.jp>  
  
ADD docker-start.sh /docker-start.sh  
RUN chmod -v +x /docker-start.sh  
  
VOLUME /usr/local/projects  
WORKDIR /usr/local/projects  
  
EXPOSE 80  
CMD ["/docker-start.sh"]  

