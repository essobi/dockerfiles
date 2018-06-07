FROM openjdk:8-jdk  
  
# add our user and group first to make sure their IDs get assigned
consistently, regardless of whatever dependencies get added  
ENV JETTY_HOME /usr/local/jetty  
ENV PATH $JETTY_HOME/bin:$PATH  
WORKDIR $JETTY_HOME  
  
ENV JETTY_VERSION 9.3.12.v20160915  
ENV JETTY_TGZ_URL https://repo1.maven.org/maven2/org/eclipse/jetty/jetty-
distribution/$JETTY_VERSION/jetty-distribution-$JETTY_VERSION.tar.gz  
ENV JETTY_BASE /var/lib/jetty  
ENV TMPDIR /tmp/jetty  
  
RUN set -xe \  
&& groupadd -r jetty && useradd -r -g jetty jetty \  
&& mkdir -p "$JETTY_HOME" \  
&& curl -SL "$JETTY_TGZ_URL" -o jetty.tar.gz \  
&& tar -xvf jetty.tar.gz --strip-components=1 \  
&& sed -i '/jetty-logging/d' etc/jetty.conf \  
&& rm -fr demo-base javadoc \  
&& rm jetty.tar.gz* \  
&& mkdir -p "$JETTY_BASE" \  
&& mkdir -p "$TMPDIR" \  
&& chown -R jetty:jetty "$TMPDIR" "$JETTY_BASE"  
WORKDIR $JETTY_BASE  
  
# Get the list of modules in the default start.ini and build new base with
those modules, then add setuid  
RUN modules="$(grep -- ^--module= "$JETTY_HOME/start.ini" | cut -d= -f2 |
paste -d, -s)" \  
&& set -xe \  
&& java -jar "$JETTY_HOME/start.jar" \--add-to-startd="$modules,setuid"  
  
COPY /docker-entrypoint.sh /  
  
EXPOSE 8080  
ENTRYPOINT ["/docker-entrypoint.sh"]  
CMD ["java","-jar","/usr/local/jetty/start.jar"]  

