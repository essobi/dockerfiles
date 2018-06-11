FROM dockerfile/java  
MAINTAINER Jordan Li  
RUN wget -O /opt/master.zip
https://github.com/eBay/restsuperman/archive/master.zip && cd /opt && unzip
master.zip  
RUN rm -rf /opt/master.zip  
RUN chmod +x /opt/restcommander-master/play-1.2.4/play  
ADD ./run.sh /usr/bin/run  
RUN chmod u+x /usr/bin/run  
CMD /usr/bin/run  
EXPOSE 9000  

