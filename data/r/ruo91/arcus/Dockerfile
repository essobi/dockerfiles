#  
# Dockerfile - Arcus  
#  
# 기본 이미지  
FROM ubuntu:14.04  
# 메인테이너  
MAINTAINER Yongbok Kim <ruo91@yongbok.net>  
  
# 기본 저장소 변경  
RUN sed -i 's/archive.ubuntu.com/ftp.jaist.ac.jp/g' /etc/apt/sources.list  
  
# 최신 패키지 업데이트 및 Arcus를 빌드하기 위한 패키지 설치  
RUN apt-get update && apt-get install -y supervisor openssh-server aptitude
net-tools iputils-ping nano curl \  
git netcat build-essential make gcc g++ autoconf automake libtool libextutils-
pkgconfig-perl libcppunit-dev python2.7-dev python-setuptools subversion  
  
# 기본 소스 디렉토리 설정  
ENV SRC_DIR /opt  
  
# JDK 설치  
ENV JAVA_HOME /usr/local/jdk  
ENV PATH $PATH:$JAVA_HOME/bin  
RUN curl -LO "http://download.oracle.com/otn-
pub/java/jdk/8u11-b12/jdk-8u11-linux-x64.tar.gz" -H 'Cookie:
oraclelicense=accept-securebackup-cookie' \  
&& tar xzf jdk-8u11-linux-x64.tar.gz && mv jdk1.8.0_11 /usr/local/jdk && rm -f
jdk-8u11-linux-x64.tar.gz \  
&& echo '' >> /etc/profile \  
&& echo '# JDK' >> /etc/profile \  
&& echo "export JAVA_HOME=$JAVA_HOME" >> /etc/profile \  
&& echo 'export PATH=$PATH:$JAVA_HOME/bin' >> /etc/profile \  
&& echo '' >> /etc/profile  
  
# ANT 설치  
ENV ANT_VER 1.9.4  
ENV ANT_HOME $SRC_DIR/apache-ant-$ANT_VER  
ENV PATH $PATH:$ANT_HOME/bin  
RUN cd $SRC_DIR && curl -LO
"http://www.us.apache.org/dist/ant/binaries/apache-ant-$ANT_VER-bin.tar.bz2" \  
&& tar xjf apache-ant-$ANT_VER-bin.tar.bz2 && rm -f apache-ant-$ANT_VER-
bin.tar.bz2 \  
&& echo '# Ant' >> /etc/profile \  
&& echo "export ANT_HOME=$ANT_HOME" >> /etc/profile \  
&& echo 'export PATH=$PATH:$ANT_HOME/bin' >> /etc/profile \  
&& echo '' >> /etc/profile  
  
# Arcus 빌드  
RUN cd $SRC_DIR && git clone https://github.com/ruo91/arcus.git \  
&& cd arcus/scripts && ./build.sh  
ADD conf/ruo91.json $SRC_DIR/arcus/scripts/conf/ruo91.json  
  
# SSH Public Key 생성  
RUN ssh-keygen -t dsa -P '' -f "/root/.ssh/id_dsa"  
RUN cat /root/.ssh/id_dsa.pub >> /root/.ssh/authorized_keys  
RUN chmod 644 /root/.ssh/authorized_keys  
  
# Supervisor 설정  
RUN mkdir -p /var/log/supervisor  
ADD conf/supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
# SSH 설정  
RUN mkdir /var/run/sshd  
RUN sed -i 's/without-password/yes/g' /etc/ssh/sshd_config  
RUN sed -i 's/UsePAM yes/UsePAM no/g' /etc/ssh/sshd_config  
  
# 루트 비밀번호 설정  
RUN echo 'root:arcus' |chpasswd  
  
# 포트 설정  
EXPOSE 22  
# 명령 실행  
CMD ["/usr/bin/supervisord"]

