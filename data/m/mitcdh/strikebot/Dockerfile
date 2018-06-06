FROM perl:latest  
MAINTAINER Mitchell Hewes <me@mitcdh.com>  
  
RUN cpanm POE::Component::IRC  
  
COPY files/* /usr/src/strikebot/  
  
WORKDIR /usr/src/strikebot  
  
USER nobody  
CMD [ "perl", "./strikebot.pl" ]

