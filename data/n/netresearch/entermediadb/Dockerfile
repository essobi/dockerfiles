FROM openjdk:jre  
  
RUN sed -i "s/httpredir.debian.org/`curl -s -D -
http://httpredir.debian.org/demo/debian/ | awk '/^Link:/ { print $2 }' | sed
-e 's@<http://\\(.*\\)/debian/>;@\1@g'`/" /etc/apt/sources.list \  
&& echo "deb http://www.deb-multimedia.org jessie main non-free" >>
/etc/apt/sources.list \  
&& echo "deb-src http://www.deb-multimedia.org jessie main non-free" >>
/etc/apt/sources.list \  
&& echo "deb http://packages.entermediadb.org/repo/apt stable main" >>
/etc/apt/sources.list \  
&& gpg --quiet --keyserver pgp.mit.edu --recv-keys 5C808C2B65558117 \  
&& gpg --quiet --armor --export 5C808C2B65558117 | apt-key add - \  
&& wget --quiet -O /etc/apt/trusted.gpg.d/entermediadb.gpg
http://packages.entermediadb.org/repo/apt/entermediadb.gpg \  
&& apt-get update \  
&& apt-get install -y --force-yes --no-install-recommends entermediadb rsync \  
&& apt-get autoremove -y \  
&& apt-get clean all \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN useradd -ms /bin/bash entermedia  
  
RUN sed -i 's/esac/foreground)\nsu $TOMCAT7_USER -c
"$CATALINA_BASE\/bin\/catalina.sh run"\n;;\nesac/'
/usr/share/entermediadb/tomcat/bin/tomcat.template  
  
RUN cp -rp "/usr/share/entermediadb/conf/ffmpeg" "/home/entermedia/.ffmpeg" \  
&& mv /etc/ImageMagick-6/delegates.xml /etc/ImageMagick-6/delegates.old \  
&& cp -p "/usr/share/entermediadb/conf/im/delegates.xml" /etc/ImageMagick-6/  
  
EXPOSE 8080  
COPY overrides /overrides  
  
COPY entrypoint.sh /entrypoint.sh  
RUN chmod +x /entrypoint.sh  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["/opt/entermediadb/tomcat/bin/tomcat", "foreground"]

