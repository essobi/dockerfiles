#furywolf/centosprod 기반으로 만든 furywolf/centosprod_wildfly 이미지  
FROM furywolf/centosprod  
  
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
  
# wildfly를 서비스로 등록시켜 systemctl을 이용해서 제어가 되도록 한다(systemctl start wildfly,
systemctl stop wildfly, systemctl restart wildfly)  
# 이때 wildfly의 관리자 계정(admin / admin)을 add-user.sh 스크립트를 실행시켜서 등록을 시켜준다  
# 그래서 wildfly의 관리자 사이트(http://ip주소:9990)을 접속해서 관리자 사이트를 로그인 할 때 이 admin /
admin 계정을 쓸 수 있게 해준다  
ADD resources/launch.sh /opt/jboss/wildfly/bin/launch.sh  
ADD resources/wildfly.conf /etc/systemd/system/wildfly.conf  
ADD resources/wildfly.service /etc/systemd/system/wildfly.service  
RUN chmod +x /opt/jboss/wildfly/bin/launch.sh \  
&& bash -c "/opt/jboss/wildfly/bin/add-user.sh admin admin" \  
&& systemctl enable wildfly  
  
#SSH 포트 21, 22, 8080, 9990, 64000-64010번 열기(8787번은 Debug에 사용할 포트로 미리 열어둔다(실제
디버그 설정은 컨테이너 안에서 설정))  
EXPOSE 21 22 8787 8080 9990 64000-64010  
ADD resources/init.sh /usr/local/bin/init.sh  
RUN chmod +x /usr/local/bin/init.sh  
ENTRYPOINT ["/usr/local/bin/init.sh"]  

