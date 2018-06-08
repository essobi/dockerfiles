FROM openshift/base-centos7  
  
MAINTAINER Martin Rumanek <martin@rumanek.cz>  
ENV TOMCAT_MAJOR=8 \  
TOMCAT_VERSION=8.5.11 \  
CATALINA_HOME=/usr/local/tomcat \  
JAVA_TOOL_OPTIONS=-Dfile.encoding=UTF8 \  
JDBC_DRIVER_DOWNLOAD_URL=https://jdbc.postgresql.org/download/postgresql-9.4.1212.jar
\  
MAVEN_VERSION=3.3.9 \  
DJATOKA_HOME=/opt/app-root/src/.meditor/djatoka \  
LD_LIBRARY_PATH=/opt/app-root/src/.meditor/djatoka/lib/Linux-x86-64 \  
KAKADU_HOME=/opt/app-root/src/.meditor/djatoka/bin/Linux-x86-64 \  
KAKADU_LIBRARY_PATH=-DLD_LIBRARY_PATH=/opt/app-
root/src/.meditor/djatoka/lib/Linux-x86-64 \  
UMASK=0002 \  
HOME=/opt/app-root/src  
  
ENV JAVA_OPTS -Djava.awt.headless=true -Dfile.encoding=UTF8 -Xms1024m
-Xmx3072m -Dkakadu.home=$KAKADU_HOME -Djava.library.path=$LD_LIBRARY_PATH
$KAKADU_LIBRARY_PATH -Duser.home=$HOME  
  
  
ENV
TOMCAT_TGZ_URL=https://www.apache.org/dist/tomcat/tomcat-$TOMCAT_MAJOR/v$TOMCAT_VERSION/bin/apache-
tomcat-$TOMCAT_VERSION.tar.gz  
  
# Set the labels that are used for Openshift to describe the builder image.  
LABEL io.k8s.description="MEditor" \  
io.k8s.display-name="MEditor" \  
io.openshift.expose-services="8080:http" \  
io.openshift.tags="builder,meditor" \  
io.openshift.s2i.scripts-url="image:///usr/libexec/s2i"  
  
# exiftool  
RUN yum install -y perl-CPAN \  
&& wget http://www.sno.phy.queensu.ca/~phil/exiftool/Image-
ExifTool-10.20.tar.gz \  
&& tar -xzf Image-ExifTool-10.20.tar.gz \  
&& cd Image-ExifTool-10.20 \  
&& perl Makefile.PL \  
&& make install \  
&& cd .. \  
&& rm -r Image-ExifTool-10.20 \  
&& rm Image-ExifTool-10.20.tar.gz  
  
RUN INSTALL_PKGS="tar sox xmlstarlet" && \  
yum install -y epel-release && \  
yum install -y --enablerepo=centosplus $INSTALL_PKGS && \  
rpm -V $INSTALL_PKGS && \  
yum clean all -y && \  
(curl -fSL
https://www.apache.org/dist/maven/maven-3/$MAVEN_VERSION/binaries/apache-
maven-$MAVEN_VERSION-bin.tar.gz | \  
tar -zx -C /usr/local) && \  
ln -sf /usr/local/apache-maven-$MAVEN_VERSION/bin/mvn /usr/local/bin/mvn  
  
WORKDIR $CATALINA_HOME  
  
RUN curl -fSL "$TOMCAT_TGZ_URL" -o tomcat.tar.gz && \  
curl -fSL "$TOMCAT_TGZ_URL.asc" -o tomcat.tar.gz.asc && \  
tar -xvf tomcat.tar.gz --strip-components=1 && \  
rm bin/*.bat && \  
rm tomcat.tar.gz  
  
RUN curl -fsL "$JDBC_DRIVER_DOWNLOAD_URL" -o
$CATALINA_HOME/lib/postgresql-9.4-1201.jdbc41.jar  
  
# because openjdk doesn't work
https://sourceforge.net/p/djatoka/mailman/djatoka-general/  
# beware updating JDK (https://github.com/xbib/marc/issues/1)  
RUN curl -v -j -k -fsL -H "Cookie: oraclelicense=accept-securebackup-cookie"
http://download.oracle.com/otn-pub/java/jdk/8u92-b14/jdk-8u92-linux-x64.rpm >
/tmp/jdk-8u92-linux-x64.rpm && \  
rpm -Uvh /tmp/jdk-8u92-linux-x64.rpm && \  
rm /tmp/jdk-8u92-linux-x64.rpm  
  
# RemoteIpValve, RewriteValve  
ADD rewrite.config $CATALINA_HOME/conf/Catalina/localhost/  
ADD server.xml $CATALINA_HOME/conf/  
  
RUN mkdir -p $HOME/.meditor  
  
# https://github.com/docker/compose/issues/3270  
RUN mkdir -p /data/imageserver  
  
# want empty properties configuration  
RUN touch $HOME/.meditor/configuration.properties  
ADD ldap.properties $HOME/.meditor/ldap.properties  
  
# z39.50  
ADD indexdata.repo /etc/yum.repos.d/indexdata.repo  
RUN rpm --import http://ftp.indexdata.com/pub/yum/centos/7/RPM-GPG-KEY-
indexdata  
RUN yum -y install libyaz5  
RUN yum -y install epel-release && rpm -Uvh
http://li.nux.ro/download/nux/dextop/el7/x86_64/nux-dextop-
release-0-5.el7.nux.noarch.rpm  
RUN yum -y --enablerepo=nux-dextop install ffmpeg  
RUN yum -y install libtiff-tools ImageMagick  
ADD libyaz4j.so $HOME/lib/libyaz4j.so  
  
COPY ["run", "assemble", "save-artifacts", "usage", "/usr/libexec/s2i/"]  
  
RUN chown -R 1001:0 $HOME $CATALINA_HOME /data/imageserver  
RUN chmod -R go=u+rw $HOME $CATALINA_HOME /data/imageserver  
  
USER 1001  
EXPOSE 8080  
CMD ["/usr/libexec/s2i/usage"]  
  

