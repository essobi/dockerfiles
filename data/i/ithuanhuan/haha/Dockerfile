# Version: 1.0.1  
FROM ubuntu:latest  
MAINTAINER xxh "xxh@qq.com"  
#ÉèÖÃrootÓÃ»§ÎªºóÐøÃüÁîµÄÖ´ÐÐÕß  
USER root  
#Ö´ÐÐ²Ù×÷  
RUN apt-get update  
RUN apt-get install -y nginx  
#Ê¹ÓÃ&&Æ´½ÓÃüÁî  
RUN touch test.txt && echo "abc" >> abc.txt  
#¶ÔÍâ±©Â¶¶Ë¿Ú  
EXPOSE 80 8080 1038  
#Ìí¼ÓÎÄ¼þ  
ADD abc.txt /opt/  
#Ìí¼ÓÎÄ¼þ¼Ð  
#ADD /webapp /opt/webapp  
#Ìí¼ÓÍøÂçÎÄ¼þ  
ADD https://www.baidu.com/img/bd_logo1.png /opt/  
#ÉèÖÃ»·¾³±äÁ¿  
ENV WEBAPP_PORT=9090  
#ÉèÖÃ¹¤×÷Ä¿Â¼  
WORKDIR /opt/  
#ÉèÖÃÆô¶¯ÃüÁî  
ENTRYPOINT ["ls"]  
#ÉèÖÃÆô¶¯²ÎÊý  
CMD ["-a", "-l" ]  
#ÉèÖÃ¾í  
VOLUME ["/data", "/var/www"]  
#ÉèÖÃ×Ó¾µÏñµÄ´¥·¢²Ù×÷  
ONBUILD ADD . /app/src  
ONBUILD RUN echo "on build excuted" >> onbuild.txt

