#furywolf/centosprod 기반으로 만든 furywolf/centosprod_svn_jenkins_nexus 이미지  
#svn server, jenkins, nexus가 같이 설치된 이미지  
#성격상 background 에서 컨테이너가 실행되어야 하기 때문에 furywolf/centosprod 를 base 이미지로 삼았다  
FROM furywolf/centosprod  
  
MAINTAINER Terry Chang <furywolf@hanmail.net>  
  
#Nexus 설치 관련 변수를 설정한다  
ARG NEXUS_VERSION=2.14.6-02  
ARG
NEXUS_DOWNLOAD_URL=https://download.sonatype.com/nexus/oss/nexus-${NEXUS_VERSION}-bundle.tar.gz  
ENV NEXUS_HOME=/home/nexus  
  
RUN yum clean all && \  
yum update -y && \  
rm -rf /var/cache/yum && \  
yum install -y initscripts  
  
#환경변수를 설정하는 environment.sh 파일을 넣어둔다(여기서 PATH를 설정한다)  
COPY resources/environment.sh /etc/profile.d/  
RUN chmod +x /etc/profile.d/environment.sh  
  
#jenkins, subversion을 설치한다  
RUN wget -O /etc/yum.repos.d/jenkins.repo https://pkg.jenkins.io/redhat-
stable/jenkins.repo && \  
rpm --import https://pkg.jenkins.io/redhat-stable/jenkins.io.key && \  
yum install -y jenkins && \  
yum install -y subversion && \  
systemctl enable svnserve.service  
  
#furywolf/centosprod 이미지가 이미 ko_KR.utf8로 locale이 설정되어 있지만 기존 설치되어 있는 package를
업데이트 하는 과정에서  
#locale이 다시 설정되어서 ko_KR.utf8 locale이 없어지는 문제가 있다  
#그래서 locale을 다시 설정한다  
RUN localedef -c -i ko_KR -f UTF-8 ko_KR.utf8  
  
#SVN Home Directory를 만든다  
RUN mkdir /home/svn  
  
#위에서 만든 SVN Home Directory로 SVN Config 파일에 설정한다  
RUN sed -i 's/\/var\/svn/\/home\/svn/g' /etc/sysconfig/svnserve  
  
#Nexus 서비스 파일을 복사한다  
ADD resources/nexus.conf /etc/systemd/system/nexus.conf  
ADD resources/nexus.service /etc/systemd/system/nexus.service  
  
#Nexus를 설치한다  
RUN mkdir -p /opt/sonatype/nexus && \  
wget ${NEXUS_DOWNLOAD_URL} && \  
tar zxvf nexus-${NEXUS_VERSION}-bundle.tar.gz && \  
mv nexus-${NEXUS_VERSION}/* /opt/sonatype/nexus/ && \  
mv sonatype-work /opt/sonatype && \  
rm -rf nexus* && \  
useradd -r -u 200 -m -c "nexus role account" -d ${NEXUS_HOME} -s /bin/false
nexus && \  
chown -R nexus:nexus /opt/sonatype && \  
systemctl enable nexus  
  
#nexus 실행 계정을 nexus 계정으로 설정하고 nexus의 context-path를 /로 설정한다  
RUN sed -i 's/#RUN_AS_USER=/RUN_AS_USER="nexus"/g'
/opt/sonatype/nexus/bin/nexus && \  
sed -i 's/nexus-webapp-context-path=\/nexus/nexus-webapp-context-path=\//g'
/opt/sonatype/nexus/conf/nexus.properties  
  
# Jenkins의 경우 Jenkins를 실행하는 계정이 root가 아닌 jenkins로 실행되기 때문에  
# Jenkins가 maven을 이용하는 build 과정에서 maven central을 통해 가져온 라이브러리를 maven
repository에 저장하지 못하는 상황이 발생한다  
# 그 이유는 maven repository 디렉토리가 root 계정 소유로 되어 있고 권한이 755로 되어 있기 때문이다  
# 그래서 권한을 777으로 바꾸어 jenkins 계정이 maven repository에 저장되도록 설정한다  
# read, write만 주면 될꺼라 생각해서 666으로 주었는데 pom.xml에서 parent를 받을 경우 이에 대해 maven에서
무언가 실행하는 것이 있는듯 하다  
RUN chmod 777 /opt/maven/repository  
  
# Host OS와 공유할 디렉토리를 만든다  
RUN mkdir /mnt/shared/jenkins && \  
mkdir /mnt/shared/svn && \  
mkdir /mnt/shared/nexus  
  
# 공유할 디렉토리가 밖으로 연결이 되도록 설정한다  
VOLUME ["/mnt/shared/jenkins", "/mnt/shared/svn", "/mnt/shared/nexus"]  
  
#SSH 포트 21, 22, 3690(svn), 8080(jenkins), 8081(nexus), 64000-64010번 열기  
EXPOSE 21 22 3690 8080 8081 64000-64010  
ADD resources/init.sh /usr/local/bin/init.sh  
RUN chmod +x /usr/local/bin/init.sh  
ENTRYPOINT ["/usr/local/bin/init.sh"]

