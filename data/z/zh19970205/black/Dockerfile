FROM tutum/lamp  
  
MAINTAINER Trumpet <zh19970205@126.com>  
  
RUN apt-get update && apt-get install -y gcc  
RUN rm -fr /app && git clone https://github.com/zh19970205/black_zhang.git
/app  
  
EXPOSE 80 3306  
CMD ["/run.sh"]  

