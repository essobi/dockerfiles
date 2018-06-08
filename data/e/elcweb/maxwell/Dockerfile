FROM java:8-jre  
  
ENV VERSION=1.7.1  
ENV
MAXWELL_URL=https://github.com/zendesk/maxwell/releases/download/v${VERSION}/maxwell-${VERSION}.tar.gz  
  
ADD $MAXWELL_URL /root/  
RUN tar -zxvf /root/maxwell-${VERSION}.tar.gz  
RUN rm /root/maxwell-${VERSION}.tar.gz  
RUN mv /maxwell-${VERSION} /code  
ADD ./start.sh /start.sh  
WORKDIR /code  
  
ENV DB_HOST=db  
ENV DB_USER=maxwell  
ENV DB_PASS=maxwell  
  
CMD ["/start.sh"]  

