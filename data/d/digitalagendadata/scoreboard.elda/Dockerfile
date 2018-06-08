FROM openjdk:8  
ENV ELDA_VERSION=1.2.21  
ENV ELDA_HOME=/var/local/elda  
  
RUN mkdir -p $ELDA_HOME \  
&& cd $ELDA_HOME \  
&& wget -nv -N -P /usr/local/bin https://storage.googleapis.com/google-code-
archive-downloads/v2/code.google.com/elda/elda-standalone-$ELDA_VERSION.jar \  
&& jar xf /usr/local/bin/elda-standalone-$ELDA_VERSION.jar \  
&& sed -i "s/hello::specs\/hello-world.ttl/specs\/scoreboard.ttl/g"
webapps/elda/WEB-INF/web.xml \  
&& sed -i "/,.*\\.ttl/d" webapps/elda/WEB-INF/web.xml \  
&& sed -i "s/url=E1.2.19-index.html/url=E1.2.21-index.html/g"
webapps/elda/lda-assets/docs/quickstart.html \  
&& for f in webapps/elda/lda-assets/images/grey/16x16/*%20*; do
newname="$(echo $f | sed s/%20/\ /)";mv "$f" "$newname"; done  
  
  
COPY elda-scoreboard.ttl $ELDA_HOME/webapps/elda/specs/scoreboard.ttl  
  
COPY docker-entrypoint.sh /  
  
EXPOSE 8080  
ENTRYPOINT ["/docker-entrypoint.sh"]  
CMD ["java", "-jar", "start.jar"]  
  

