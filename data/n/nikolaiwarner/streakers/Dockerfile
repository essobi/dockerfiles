FROM stackbrew/ubuntu:trusty  
  
MAINTAINER Nick Warner <nickwarner@gmail.com>  
  
RUN apt-get update  
RUN apt-get install -y golang git mercurial  
  
ENV GOPATH /go  
ENV PATH $PATH:/usr/local/go/bin:$GOPATH/bin  
  
RUN mkdir -p /var/www  
RUN chown -R www-data:www-data /var/www  
  
ADD * /var/www/  
RUN chmod +x /var/www/entrypoint.sh  
  
ENTRYPOINT /var/www/entrypoint.sh  
CMD []  
  
EXPOSE 3000  

