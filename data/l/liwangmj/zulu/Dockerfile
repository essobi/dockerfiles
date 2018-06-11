# centos  
FROM registry.cn-hangzhou.aliyuncs.com/basic/centos:latest  
  
# author  
MAINTAINER Wim Li <liwangmj@gmail.com> (http://liwangmj.com)  
  
# copy  
ADD zulu8.23.0.3-jdk8.0.144-linux_x64.tar.gz /tmp/  
COPY ZuluJCEPolicies.zip /tmp/  
COPY install_zcck.sh /tmp/  
COPY zcck8.0.0.4-linux_x64.sh /tmp/  
ADD apache-ant-1.9.7-bin.tar.gz /tmp/  
ADD apache-maven-3.3.9-bin.tar.gz /tmp/  
COPY gradle-3.1-all.zip /tmp/  
  
# install zulu  
RUN set -x \  
&& echo '==> install zulu' \  
&& cd /tmp \  
&& chmod 755 -R zulu8.23.0.3-jdk8.0.144-linux_x64 \  
&& mv zulu8.23.0.3-jdk8.0.144-linux_x64 /usr/local/zulu \  
&& echo '==> install jce policies' \  
&& cd /tmp \  
&& unzip ZuluJCEPolicies.zip \  
&& chmod 755 -R ZuluJCEPolicies \  
&& \cp -rfp ZuluJCEPolicies/* /usr/local/zulu/jre/lib/security/ \  
&& echo '==> install zcck' \  
&& chmod 755 install_zcck.sh \  
&& chmod 755 zcck8.0.0.4-linux_x64.sh \  
&& ./install_zcck.sh \  
&& echo '==> install ant' \  
&& cd /tmp \  
&& chmod 755 -R apache-ant-1.9.7 \  
&& mv apache-ant-1.9.7 /usr/local/ant \  
&& echo '==> install maven' \  
&& cd /tmp \  
&& chmod 755 -R apache-maven-3.3.9 \  
&& mv apache-maven-3.3.9 /usr/local/maven \  
&& echo '==> install gradle' \  
&& cd /tmp \  
&& unzip gradle-3.1-all.zip \  
&& chmod 755 -R gradle-3.1 \  
&& mv gradle-3.1 /usr/local/gradle \  
&& echo '==> clean' \  
&& rm -rf /tmp/*  
  
# env  
ENV JAVA_HOME /usr/local/zulu  
ENV JRE_HOME $JAVA_HOME/jre  
ENV JAVA_FONTS $JRE_HOME/lib/fonts  
ENV CLASSPATH .:$JAVA_HOME/lib/dt.jar:$JAVA_HOME/lib/tools.jar:$JRE_HOME/lib  
ENV ANT_HOME /usr/local/ant  
ENV MAVEN_HOME /usr/local/maven  
ENV GRADLE_HOME /usr/local/gradle  
ENV PATH
$GRADLE_HOME/bin:$MAVEN_HOME/bin:$ANT_HOME/bin:$JAVA_HOME/bin:$JRE_HOME/bin:$PATH  

