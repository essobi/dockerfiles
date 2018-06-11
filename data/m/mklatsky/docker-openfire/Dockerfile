FROM mostalive/ubuntu-14.04-oracle-jdk8  
MAINTAINER mklatsky@esperdyne.com  
  
ENV OPENFIRE_VERSION 4.0.2  
RUN apt-get update \  
&& apt-get install -y openjdk-7-jre \  
&& wget
"http://www.igniterealtime.org/downloadServlet?filename=openfire/openfire_${OPENFIRE_VERSION}_all.deb"
\  
-O /tmp/openfire_${OPENFIRE_VERSION}_all.deb \  
&& dpkg -i /tmp/openfire_${OPENFIRE_VERSION}_all.deb \  
&& rm -rf openfire_${OPENFIRE_VERSION}_all.deb \  
&& rm -rf /var/lib/apt/lists/* # 20140918  
  
ADD start /start  
RUN chmod 755 /start  
  
EXPOSE 3478  
EXPOSE 3479  
EXPOSE 5222  
EXPOSE 5223  
EXPOSE 5229  
EXPOSE 7070  
EXPOSE 7443  
EXPOSE 7777  
EXPOSE 9090  
EXPOSE 9091  
#  
VOLUME ["/opt/openfire/data"]  
CMD ["/start"]  

