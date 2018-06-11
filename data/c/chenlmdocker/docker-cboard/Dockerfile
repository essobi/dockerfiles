FROM centos:7.2.1511  
WORKDIR /root  
  
ARG CBOARD_BRANCH=branch-0.4.2-nfq  
  
# 安装 java maven  
RUN mv /etc/yum.repos.d/CentOS-Base.repo /etc/yum.repos.d/CentOS-
Base.repo.backup \  
&& curl -o /etc/yum.repos.d/CentOS-Base.repo
http://mirrors.aliyun.com/repo/Centos-7.repo  
RUN yum install -y java-1.8.0-openjdk.x86_64 java-1.8.0-openjdk-devel.x86_64
wget vim git  
RUN wget http://repos.fedorapeople.org/repos/dchen/apache-maven/epel-apache-
maven.repo -O /etc/yum.repos.d/epel-apache-maven.repo \  
&& yum -y install apache-maven  
  
# 下载源码切换分支  
RUN git clone -b ${CBOARD_BRANCH} \--single-branch
https://github.com/chenlingmin/CBoard.git  
  
# 编译代码  
RUN mvn -f /root/CBoard/pom.xml clean package && yes|cp /root/CBoard/lib/*.jar
/root/CBoard/target/cboard/WEB-INF/lib/  
  
# 安装tomcat phantomjs  
RUN wget http://mirror.bit.edu.cn/apache/tomcat/tomcat-8/v8.0.52/bin/apache-
tomcat-8.0.52.tar.gz -P install \  
&& wget
https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-linux-x86_64.tar.bz2
-P install  
  
RUN yum install -y bzip2.x86_64  
  
RUN tar -zxf install/apache-tomcat-8.0.52.tar.gz -C /opt \  
&& tar -jxf install/phantomjs-2.1.1-linux-x86_64.tar.bz2 -C /opt \  
&& ln -s /opt/apache-tomcat-8.0.52 /opt/apache-tomcat \  
&& ln -s /opt/phantomjs-2.1.1-linux-x86_64 /opt/phantomjs-2.1.1  
  
RUN rm -rf /opt/apache-tomcat-8.0.52/webapps/*  
RUN mv /root/CBoard/target/cboard /cboard && ln -s /cboard /opt/apache-
tomcat-8.0.52/webapps/ROOT  
  
RUN yum remove -y apache-maven bzip2.x86_64 java-1.8.0-openjdk-devel.x86_64
git wget vim  
RUN rm -rf /root/CBoard /root/.m2/ /root/install  
  
COPY docker-entrypoint.sh ./  
RUN chmod +x ./docker-entrypoint.sh  
  
EXPOSE 8080  
CMD ["/root/docker-entrypoint.sh"]  

