FROM java:7-jre  
  
ENV CROWD_VERSION 2.8.0  
ENV CROWD_DOWNLOAD_URL
http://www.atlassian.com/software/crowd/downloads/binary/atlassian-
crowd-$CROWD_VERSION.tar.gz  
  
RUN set -x \  
&& mkdir -p /opt/crowd \  
&& mkdir -p /home/crowd \  
&& ( curl -sSL $CROWD_DOWNLOAD_URL | tar -xzf - -C /opt/crowd --strip-
components=1 ) \  
&& sed -i "s:#crowd.home=/var/crowd-home:crowd.home=/home/crowd:g"
/opt/crowd/crowd-webapp/WEB-INF/classes/crowd-init.properties  
  
ADD entrypoint.sh /entrypoint.sh  
RUN chmod +x /entrypoint.sh  
  
VOLUME /home/crowd  
  
EXPOSE 8095  
WORKDIR /home/crowd  
  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["crowd"]  

