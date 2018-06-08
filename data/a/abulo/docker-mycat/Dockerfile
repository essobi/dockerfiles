FROM java:8-jre  
MAINTAINER abulo.hoo@gmail.com  
LABEL Description="使用mycat做mysql数据库的读写分离"  
#ENV mycat-version Mycat-server-1.6-RELEASE-20161028204710-linux.tar.gz  
USER root  
#COPY ./Mycat-server-1.6-RELEASE-20161028204710-linux.tar.gz /  
RUN cd /usr/local && wget http://dl.mycat.io/1.6-RELEASE/Mycat-
server-1.6-RELEASE-20161028204710-linux.tar.gz && tar -zxf Mycat-
server-1.6-RELEASE-20161028204710-linux.tar.gz  
ENV MYCAT_HOME=/usr/local/mycat  
ENV PATH=$PATH:$MYCAT_HOME/bin  
WORKDIR $MYCAT_HOME/bin  
RUN chmod u+x ./mycat  
EXPOSE 8066 9066  
CMD ["./mycat","console"]  

