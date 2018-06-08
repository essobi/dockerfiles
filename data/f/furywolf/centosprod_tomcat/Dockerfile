#furywolf/centosprod 기반으로 만든 furywolf/centosprod_tomcat 이미지  
FROM furywolf/centosprod  
  
MAINTAINER Terry Chang <furywolf@hanmail.net>  
  
ENV TOMCAT_VERSION_MAJOR=8 \  
TOMCAT_VERSION=8.5.27 \  
CATALINA_HOME=/opt/tomcat \  
JPDA_ADDRESS=8000  
RUN yum clean all && \  
yum update -y && \  
rm -rf /var/cache/yum  
  
#환경변수를 설정하는 environment.sh 파일을 넣어둔다(여기서 PATH를 설정한다)  
COPY resources/environment.sh /etc/profile.d/  
RUN chmod +x /etc/profile.d/environment.sh  
  
#tomcat 설치  
RUN mkdir -p $CATALINA_HOME \  
&& curl -O
http://mirror.navercorp.com/apache/tomcat/tomcat-$TOMCAT_VERSION_MAJOR/v$TOMCAT_VERSION/bin/apache-
tomcat-$TOMCAT_VERSION.tar.gz \  
&& tar xf apache-tomcat-$TOMCAT_VERSION.tar.gz \  
&& mv apache-tomcat-$TOMCAT_VERSION/* $CATALINA_HOME \  
&& rm -rf apache-tomcat-$TOMCAT_VERSION \  
&& rm apache-tomcat-$TOMCAT_VERSION.tar.gz  
  
ADD resources/tomcat.conf /etc/systemd/system/tomcat.conf  
ADD resources/tomcat.service /etc/systemd/system/tomcat.service  
RUN systemctl enable tomcat  
  
#Tomcat 관리자 생성 스크립트를 넣어서 실행하도록 한다(create_admin_user.sh admin adminpwd 를 실행함으로써
관리자 id가 admin, 관리자 패스워드가 adminpwd로 되도록 한다)  
ADD resources/create_admin_user.sh $CATALINA_HOME/scripts/create_admin_user.sh  
RUN chmod +x $CATALINA_HOME/scripts/create_admin_user.sh \  
&& sync && $CATALINA_HOME/scripts/create_admin_user.sh admin adminpwd  
  
#Tomcat 관리자 페이지가 접속되도록 하기 위해 기존의 context.xml이 수정된 새로운 내용의 context.xml을 복사하도록
한다  
#원래의 context.xml에서 <Valve> 태그를 주석처리한 xml 파일을 넣도록 한다  
ADD resources/context.xml /opt/tomcat/webapps/manager/META-INF/context.xml  
  
#SSH 포트 21, 22, 8080, 8009, 64000-64010번 열기(8000번은 JPDA Debug에 사용할 포트로 미리
열어둔다(실제 디버그 설정은 컨테이너 안에서 설정))  
EXPOSE 21 22 8000 8080 8009 64000-64010  
ADD resources/init.sh /usr/local/bin/init.sh  
RUN chmod +x /usr/local/bin/init.sh  
ENTRYPOINT ["/usr/local/bin/init.sh"]  

