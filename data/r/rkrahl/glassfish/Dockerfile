FROM rkrahl/opensuse:42.3  
ENV GLASSFISH_HOME /opt/glassfish4  
ENV JAVA_HOME /usr/lib64/jvm/java-1.8.0-openjdk  
  
RUN zypper --non-interactive install \  
java-1_8_0-openjdk-devel \  
mysql-connector-java \  
unzip  
  
RUN groupadd -r -g 800 glassfish && \  
useradd -r -u 800 -g glassfish -d $GLASSFISH_HOME -s /sbin/nologin \  
-c "GlassFish JavaEE application server" glassfish && \  
mkdir -p $GLASSFISH_HOME /etc/glassfish /etc/glassfish.d  
COPY start-glassfish.sh /etc/glassfish  
RUN chmod 0755 /etc/glassfish/start-glassfish.sh && \  
chown -R glassfish:glassfish \  
$GLASSFISH_HOME /etc/glassfish /etc/glassfish.d  
  
USER glassfish  
WORKDIR $GLASSFISH_HOME  
  
ENV PATH $GLASSFISH_HOME/bin:$JAVA_HOME/bin:/usr/local/bin:/usr/bin:/bin  
  
RUN tmpfile=`mktemp` && \  
curl --silent --show-error --location --output $tmpfile \  
http://download.java.net/glassfish/4.0/release/glassfish-4.0.zip && \  
unzip -q -d /opt $tmpfile && \  
rm -rf $tmpfile && \  
asadmin delete-domain domain1  
  
CMD ["/etc/glassfish/start-glassfish.sh"]  
  
VOLUME ["$GLASSFISH_HOME/glassfish/domains"]  
  
EXPOSE 4848 8009 8080 8181  

