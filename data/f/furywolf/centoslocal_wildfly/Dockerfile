#furywolf/centoslocal 기반으로 만든 furywolf/centoslocal_wildfly 이미지  
FROM furywolf/centoslocal  
  
MAINTAINER Terry Chang <furywolf@hanmail.net>  
  
ENV WILDFLY_VERSION=10.1.0.Final \  
WILDFLY_SHA1=9ee3c0255e2e6007d502223916cefad2a1a5e333 \  
JBOSS_HOME=/opt/jboss/wildfly \  
LAUNCH_JBOSS_IN_BACKGROUND=true  
  
RUN yum clean all && \  
yum update -y && \  
yum install -y xmlstarlet saxon augeas bsdtar unzip && \  
yum clean all && \  
rm -rf /var/cache/yum  
  
#환경변수를 설정하는 environment.sh 파일을 넣어둔다(여기서 PATH를 설정한다)  
COPY resources/environment.sh /etc/profile.d/  
RUN chmod +x /etc/profile.d/environment.sh  
  
#wildfly 설치  
RUN mkdir -p $JBOSS_HOME \  
&& curl -O
https://download.jboss.org/wildfly/$WILDFLY_VERSION/wildfly-$WILDFLY_VERSION.tar.gz
\  
&& sha1sum wildfly-$WILDFLY_VERSION.tar.gz | grep $WILDFLY_SHA1 \  
&& tar xf wildfly-$WILDFLY_VERSION.tar.gz \  
&& mv wildfly-$WILDFLY_VERSION/* $JBOSS_HOME \  
&& rm -rf wildfly-$WILDFLY_VERSION \  
&& rm wildfly-$WILDFLY_VERSION.tar.gz  
  
# wildfly에 Oracle JDBC 드라이버를 등록한다  
RUN mkdir -p
/opt/jboss/wildfly/modules/system/layers/base/com/oracle/ojdbc6/main  
ADD resources/oracle/module.xml
/opt/jboss/wildfly/modules/system/layers/base/com/oracle/ojdbc6/main/module.xml  
ADD resources/oracle/ojdbc6.jar
/opt/jboss/wildfly/modules/system/layers/base/com/oracle/ojdbc6/main/ojdbc6.jar  
  
# Oracje JDBC 드라이버가 반영되어 있는 수정된 standalone.xml을 넣어둔다  
ADD resources/standalone.xml
/opt/jboss/wildfly/standalone/configuration/standalone.xml  
  
# wildfly를 실행시키는 shell script를 추가한다(나중에 이 shell script를 실행시키는 걸로 wildfly를
실행한다)  
ADD resources/launch.sh /opt/jboss/wildfly/bin/launch.sh  
  
# wildfly의 관리자 계정(admin / admin)을 add-user.sh 스크립트를 실행시켜서 등록을 시켜준다  
RUN chmod +x /opt/jboss/wildfly/bin/launch.sh \  
&& bash -c "/opt/jboss/wildfly/bin/add-user.sh admin admin"  
  
# deployments 디렉토리가 밖으로 연결이 되도록 설정한다  
VOLUME ["/opt/jboss/wildfly/standalone/deployments"]  
  
#포트 8787, 8080, 9990, 64000-64010번 열기(8787번은 Debug에 사용할 포트로 미리 열어둔다(실제 디버그 설정은
컨테이너 안에서 설정))  
EXPOSE 8787 8080 9990 64000-64010  
# /opt/jboss/wildfly/bin/standalone.sh -c standalone.xml -b 0.0.0.0
-bmanagement 0.0.0.0 --debug  
ENTRYPOINT ["/opt/jboss/wildfly/bin/launch.sh"]  

