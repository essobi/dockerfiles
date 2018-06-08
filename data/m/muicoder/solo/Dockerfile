FROM muicoder/jre  
  
ARG VERSION=2.7.0  
RUN curl -fsSL https://github.com/muicoder/solo/raw/releases/solo-$VERSION.war
-o /tmp/solo.zip \  
&& mkdir -pv /solo \  
&& unzip -q /tmp/solo.zip -d /solo \  
&& sed -i "s/~//" /solo/WEB-INF/classes/local.properties \  
&& rm -fvr /tmp/*  
  
WORKDIR /solo  
VOLUME ["/solo_h2"]  
  
EXPOSE 8080  
ENTRYPOINT ["tini", "-s", "--", "java", "-cp", "WEB-INF/lib/*:WEB-
INF/classes", "org.b3log.solo.Starter"]  
CMD ["--listen_port", "8080", "--server_port", "8080"]  

