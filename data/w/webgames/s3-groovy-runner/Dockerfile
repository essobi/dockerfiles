FROM dpatriot/docker-s3-runner:1.4.1  
MAINTAINER Shago Vyacheslav <v.shago@corpwebgames.com>  
  
RUN apt-get update \  
&& apt-get install -y zip \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN curl -s get.sdkman.io | bash \  
&& echo "gvm_auto_answer=true" >> ~/.sdkman/etc/config \  
&& /bin/bash -c "source /root/.sdkman/bin/sdkman-init.sh && sdk install
groovy" \  
&& mkdir -p $HOME/.groovy/lib  
  
RUN /bin/bash -c "source /root/.sdkman/bin/sdkman-init.sh \  
&& grape install 'com.amazonaws' 'aws-java-sdk' '1.11.172' \  
&& grape install 'com.amazonaws' 'aws-java-sdk' '1.11.331' \  
&& grape install 'mysql' 'mysql-connector-java' '5.1.38' \  
&& grape install 'commons-io' 'commons-io' '2.5' \  
&& grape install 'com.sparkjava' 'spark-core' '2.3' \  
&& grape install 'org.codehaus.groovy.modules.http-builder' 'http-builder'
'0.7.1' \  
&& grape install 'ch.qos.logback' 'logback-classic' '1.2.3'"  
#load non-grape libs  
RUN curl -o $HOME/.groovy/lib/RedshiftJDBC41-1.1.10.1010.jar
https://s3.amazonaws.com/redshift-
downloads/drivers/RedshiftJDBC41-1.1.10.1010.jar  
#unload lib  
RUN rm -f /root/.sdkman/candidates/groovy/current/lib/servlet-api-2.4.jar  
#ADD import-rds-ca.sh /opt/  
#RUN chmod +x /opt/import-rds-ca.sh && /opt/import-rds-ca.sh  
  
ENV GROOVY_HOME /root/.sdkman/candidates/groovy/current  
ENV PATH $GROOVY_HOME/bin:$PATH  

