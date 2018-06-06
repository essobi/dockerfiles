FROM openjdk  
MAINTAINER Fabio Montefuscolo <fabio.montefuscolo@gmail.com>  
  
RUN wget -O /root/openfire.tar.gz
https://github.com/igniterealtime/Openfire/releases/download/v4.1.3/openfire_4_1_3.tar.gz
\  
&& tar -C /opt -zxvf /root/openfire.tar.gz \  
&& mv /opt/openfire/plugins /opt/openfire/plugins-folder \  
&& mkdir -p /opt/openfire/plugins \  
&& rm /root/openfire.tar.gz  
  
EXPOSE \  
5222 \  
5223 \  
5229 \  
5262 \  
5263 \  
5269 \  
5275 \  
5276 \  
7070 \  
7443 \  
7777 \  
9090 \  
9091  
  
VOLUME /opt/openfire/plugins  
  
ADD entrypoint.sh /entrypoint.sh  
ENTRYPOINT ["/entrypoint.sh"]  
  
CMD [ \  
"java", "-server", \  
"-DopenfireHome=/opt/openfire", \  
"-Dopenfire.lib.dir=/opt/openfire/lib", \  
"-classpath", "/opt/openfire/lib/startup.jar", \  
"-jar", "/opt/openfire/lib/startup.jar" \  
]  
  

