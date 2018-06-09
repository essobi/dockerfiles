FROM selim13/exim-relay:latest  
  
COPY ./conf.d/main.conf /etc/exim/conf.d/  
COPY ./conf.d/authenticators.conf /etc/exim/conf.d/  
COPY ./conf.d/routers.conf /etc/exim/conf.d/  
COPY ./conf.d/transports.conf /etc/exim/conf.d/  
  
ENV EXIM_GMAIL_LOGIN= \  
EXIM_GMAIL_PASSWORD=

