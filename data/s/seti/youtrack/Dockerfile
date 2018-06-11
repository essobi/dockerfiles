FROM java:latest  
  
LABEL maintainer="Seti <seti@setadesign.net>"  
  
ENV APP_BUILD 2018.1.41561  
ENV APP_HOME /data  
  
RUN curl --insecure -L
https://download.jetbrains.com/charisma/youtrack-$APP_BUILD.zip -o
/opt/youtrack.zip && \  
cd /opt && \  
unzip /opt/youtrack.zip && \  
rm -f /opt/youtrack.zip && \  
mv youtrack-* youtrack && \  
rm -rf /opt/youtrack/internal/java && \  
mkdir $APP_HOME && \  
groupadd -r youtrack && \  
useradd -r -g youtrack -u 1000 -d $APP_HOME youtrack && \  
chown -R youtrack:youtrack $APP_HOME /opt/youtrack && \  
mv /opt/youtrack/conf /opt/youtrack/conftemplate  
  
WORKDIR /opt/youtrack  
ADD run.sh /opt/youtrack/  
RUN chmod o+rx run.sh  
USER youtrack  
ENTRYPOINT ["/opt/youtrack/run.sh"]  
EXPOSE 8080  
VOLUME ["$APP_HOME"]  

