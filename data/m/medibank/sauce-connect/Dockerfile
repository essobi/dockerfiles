FROM java:8-jre  
MAINTAINER Warner Godfrey <warner.godfrey@medibank.com.au>  
  
ENV SAUCE_VERSION 4.3.15  
WORKDIR /usr/local/sauce-connect  
  
RUN curl https://saucelabs.com/downloads/sc-$SAUCE_VERSION-linux.tar.gz | tar
-xz  
  
COPY sc.sh /usr/local/sauce-connect/sc-$SAUCE_VERSION-linux/bin/  
  
WORKDIR /usr/local/sauce-connect/sc-$SAUCE_VERSION-linux  
  
ENTRYPOINT ["/usr/local/sauce-connect/sc-4.3.15-linux/bin/sc.sh"]  
  
EXPOSE 8032  
CMD []  

