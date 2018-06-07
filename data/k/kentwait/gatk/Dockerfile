# kentwait/gatk  
FROM kentwait/alpine-oraclejdk8-base  
MAINTAINER Kent Kawashima <kentkawashima@gmail.com>  
  
# Modified from https://github.com/alexcoppe/bio-
dockers/blob/master/gatk/Dockerfile  
ENV MAVEN_VERSION 3.3.9  
ENV GATK_DIR_NAME gatk-protected  
ENV GATK_VERSION 3.7  
ADD
http://mirror.nohup.it/apache/maven/maven-3/${MAVEN_VERSION}/binaries/apache-
maven-${MAVEN_VERSION}-bin.zip /tmp/  
ADD https://github.com/broadgsa/gatk-protected/archive/${GATK_VERSION}.zip
/tmp/  
  
RUN cd /opt/ && unzip /tmp/apache-maven-${MAVEN_VERSION}-bin.zip \  
&& rm -rf /tmp/apache-maven-${MAVEN_VERSION}-bin.zip LICENSE NOTICE README.txt
\  
&& cd /opt/ && unzip /tmp/${GATK_VERSION}.zip \  
&& rm -rf /tmp/${GATK_VERSION}.zip \  
&& cd /opt/${GATK_DIR_NAME}-${GATK_VERSION} && /opt/apache-
maven-${MAVEN_VERSION}/bin/mvn verify -P\\!queue \  
&& mv /opt/${GATK_DIR_NAME}-${GATK_VERSION}/protected/gatk-package-
distribution/target/gatk-package-distribution-${GATK_VERSION}.jar
/opt/GenomeAnalysisTK.jar \  
&& rm -rf /opt/${GATK_DIR_NAME}-${GATK_VERSION} /opt/apache-
maven-${MAVEN_VERSION} \  
&& rm -rf /tmp/* /var/cache/apk/*  
ENV GATK /opt/GenomeAnalysisTK.jar  
  
WORKDIR /data  
VOLUME /data  
ENTRYPOINT ["/init", "java", "-jar", "/opt/GenomeAnalysisTK.jar"]  

