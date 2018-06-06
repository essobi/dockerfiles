FROM tutum/lamp:latest  
MAINTAINER Vitor Arins <vitorarins@gmail.com>  
RUN rm -fr /app && git clone https://github.com/Datawalke/Coordino.git /app  
ADD database.php /app/app/config/database.php  
RUN apt-get update && \  
apt-get -y install php5-gd  
RUN chmod -R a+w /app  
EXPOSE 80 3306  
CMD ["/run.sh"]

