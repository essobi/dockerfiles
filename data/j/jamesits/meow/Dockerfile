FROM ubuntu:latest  
MAINTAINER James Swineson <jamesswineson@gmail.com>  
  
RUN apt-get update && apt-get upgrade -y && apt-get install -y curl \  
&& rm -rf /var/lib/apt/lists/*  
  
ENV MEOW_INSTALLDIR=/usr/local/bin  
WORKDIR /usr/local/bin  
RUN curl -L git.io/meowproxy | bash  
  
EXPOSE 4411  
COPY docker-entrypoint.sh /entrypoint.sh  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["MEOW"]  

