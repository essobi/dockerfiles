FROM centos:7  
RUN yum -y install deltarpm epel-release && yum -y update  
RUN yum -y install https://centos7.iuscommunity.org/ius-release.rpm  
RUN yum -y install python35u  
RUN yum -y install python35u-pip supervisor  
RUN cd /usr/bin && ln -s python3.5 python3 && cd -  
RUN pip3.5 install cherrypy  
RUN curl -v -j -k -L https://s3.eu-central-1.amazonaws.com/docker-
assets/dist/jdk-8u101-linux-x64.rpm > /tmp/jdk-8u101-linux-x64.rpm  
RUN yum -y install /tmp/jdk-8u101-linux-x64.rpm wget unzip \  
&& alternatives --install /usr/bin/java java /usr/java/latest/bin/java 200000
\  
&& alternatives --install /usr/bin/javaws javaws /usr/java/latest/bin/javaws
200000 \  
&& alternatives --install /usr/bin/javac javac /usr/java/latest/bin/javac
200000  
  
RUN rm -rf "$JAVA_HOME/"*src.zip  
  
RUN rm -rf "$JAVA_HOME/lib/missioncontrol" \  
"$JAVA_HOME/lib/visualvm" \  
"$JAVA_HOME/lib/"*javafx* \  
"$JAVA_HOME/jre/lib/plugin.jar" \  
"$JAVA_HOME/jre/lib/ext/jfxrt.jar" \  
"$JAVA_HOME/jre/bin/javaws" \  
"$JAVA_HOME/jre/lib/javaws.jar" \  
"$JAVA_HOME/jre/lib/desktop" \  
"$JAVA_HOME/jre/plugin" \  
"$JAVA_HOME/jre/lib/"deploy* \  
"$JAVA_HOME/jre/lib/"*javafx* \  
"$JAVA_HOME/jre/lib/"*jfx* \  
"$JAVA_HOME/jre/lib/amd64/libdecora_sse.so" \  
"$JAVA_HOME/jre/lib/amd64/"libprism_*.so \  
"$JAVA_HOME/jre/lib/amd64/libfxplugins.so" \  
"$JAVA_HOME/jre/lib/amd64/libglass.so" \  
"$JAVA_HOME/jre/lib/amd64/libgstreamer-lite.so" \  
"$JAVA_HOME/jre/lib/amd64/"libjavafx*.so \  
"$JAVA_HOME/jre/lib/amd64/"libjfx*.so && \  
rm -rf "$JAVA_HOME/jre/bin/jjs" \  
"$JAVA_HOME/jre/bin/keytool" \  
"$JAVA_HOME/jre/bin/orbd" \  
"$JAVA_HOME/jre/bin/pack200" \  
"$JAVA_HOME/jre/bin/policytool" \  
"$JAVA_HOME/jre/bin/rmid" \  
"$JAVA_HOME/jre/bin/rmiregistry" \  
"$JAVA_HOME/jre/bin/servertool" \  
"$JAVA_HOME/jre/bin/tnameserv" \  
"$JAVA_HOME/jre/bin/unpack200" \  
"$JAVA_HOME/jre/lib/ext/nashorn.jar" \  
"$JAVA_HOME/jre/lib/jfr.jar" \  
"$JAVA_HOME/jre/lib/jfr" \  
"$JAVA_HOME/jre/lib/oblique-fonts" && \  
rm "/tmp/"*  
  
RUN curl "https://s3.amazonaws.com/aws-cli/awscli-bundle.zip" -o "awscli-
bundle.zip" && unzip awscli-bundle.zip && ./awscli-bundle/install -i
/usr/local/aws -b /usr/local/bin/aws  
RUN wget -q http://apache-mirror.rbc.ru/pub/apache//jmeter/binaries/apache-
jmeter-3.1.zip  
RUN wget -q https://repo1.maven.org/maven2/kg/apc/jmeter-plugins-
manager/0.11/jmeter-plugins-manager-0.11.jar  
RUN wget -q https://repo1.maven.org/maven2/kg/apc/jmeter-plugins-
json/2.6/jmeter-plugins-json-2.6.jar  
RUN wget -q https://repo1.maven.org/maven2/org/codehaus/groovy/groovy-
all/2.4.7/groovy-all-2.4.7.jar  
  
RUN unzip apache-jmeter-3.1.zip -d ~/jmeter  
RUN mkdir -p ~/jmeter/apache-jmeter-3.1/lib/ext  
  
RUN mv jmeter-plugins-manager-0.11.jar ~/jmeter/apache-jmeter-3.1/lib/ext  
RUN mv jmeter-plugins-json-2.6.jar ~/jmeter/apache-jmeter-3.1/lib/  
RUN mv groovy-all-2.4.7.jar ~/jmeter/apache-jmeter-3.1/lib/  

