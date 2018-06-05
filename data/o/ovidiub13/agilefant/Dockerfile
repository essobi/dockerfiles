FROM tomcat:8-jre8  
MAINTAINER Ovidiu-Florin Bogdan (ovidiu.b13@gmail.com)  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV AGILEFANT_VERSION 3.5.4  
  
RUN apt update && apt install -y \  
ttf-dejavu  
  
RUN wget
https://sourceforge.net/projects/agilefant/files/Agilefant3/agilefant-$AGILEFANT_VERSION.zip/download
\  
-O /tmp/agilefant.zip  
RUN unzip /tmp/agilefant.zip -d /tmp/agilefant \  
&& rm -rf /usr/local/tomcat/webapps/ROOT \  
&& unzip /tmp/agilefant/agilefant.war -d /usr/local/tomcat/webapps/ROOT  
  
RUN rm -rf /tmp/agilefant /tmp/agilefant.zip  
  
COPY entrypoint.sh /entrypoint.sh  
  
# ENV AF_UNZIP /tmp/agilefant  
# ENV AF_UNWAR $AF_UNZIP/agilefant  
# ENV AF_CONFIG $AF_UNWAR/WEB-INF/agilefant.conf  
# ENV DESTINATION /usr/local/tomcat/webapps/agilefant  
#  
# RUN mkdir -p /tmp /opt  
# ADD
https://sourceforge.net/projects/agilefant/files/Agilefant3/agilefant-3.5.4.zip/download
/tmp/agilefant.zip  
# ADD assets/entrypoint.sh /opt/entrypoint.sh  
# ADD assets/setenv.sh /usr/local/tomcat/bin/setenv.sh  
#  
# RUN cd /tmp \  
# && unzip -d "$AF_UNZIP" agilefant.zip \  
# && cd "$AF_UNZIP" \  
# && unzip -d "$AF_UNWAR" agilefant.war \  
# && cd "$AF_UNWAR" \  
# && sed -i -e"s/localhost/db/" "$AF_CONFIG" \  
# && cp -r "$AF_UNWAR" "$DESTINATION"  
  
EXPOSE 8080  
  
ENTRYPOINT /entrypoint.sh  

