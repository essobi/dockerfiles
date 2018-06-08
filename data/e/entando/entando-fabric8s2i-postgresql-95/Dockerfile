FROM
centos/postgresql-95-centos7@sha256:2868b2293d03b09f1a3e34caedee2472f760f2d9996c917626a15ab887255f53  
LABEL io.openshift.s2i.destination="/opt/s2i/destination" \  
maintainer="Ampie Barnard <a.barnard@entando.com>" \  
io.k8s.description="Postgresql Database Image for building and running Entando
applications" \  
io.k8s.display-name="Postgresql Database Image for Entando 5"  
  
ENV MAVEN_VERSION="3.5.3" \  
JAVA_HOME="/usr/lib/jvm/java-1.8.0" \  
ENTANDO_VERSION="5.0.0"  
#Change to root for installation operations  
USER root  
RUN INSTALL_PKGS="ant tar curl java-1.8.0-openjdk java-1.8.0-openjdk-devel" &&
\  
yum install -y --enablerepo=centosplus $INSTALL_PKGS && \  
rpm -V $INSTALL_PKGS && \  
yum clean all -y && \  
(curl -v
https://www.apache.org/dist/maven/maven-3/$MAVEN_VERSION/binaries/apache-
maven-$MAVEN_VERSION-bin.tar.gz | tar -zx -C /usr/local) && \  
ln -sf /usr/local/apache-maven-$MAVEN_VERSION/bin/mvn /usr/local/bin/mvn && \  
mkdir -p /var/lib/pgsql/.m2 && chmod ug+rw /var/lib/pgsql/.m2 && chown 26:root
/var/lib/pgsql/.m2  
  
#stay in root to ensure chmod works  
COPY ./contrib/maven-setup /tmp/maven-setup  
RUN chmod -Rf ug+rw /tmp/maven-setup && chown -Rf 26:root /tmp/maven-setup  
  
#The user 'postgres' is 26, and openshift requires the numeric:  
#Run all of this as postgres as this will be the user under which the S2I
build takes place  
USER 26  
WORKDIR /tmp/maven-setup/  
RUN ./prepare_m2_repo.sh $ENTANDO_VERSION  
WORKDIR $HOME  
  
#use root to ensure chmod works  
USER root  
#Add scripts  
COPY ./contrib/common.sh /usr/share/container-scripts/postgresql/common.sh  
RUN chmod -Rf ug+rw /usr/share/container-scripts/postgresql/common.sh && chown
-Rf postgres:root /usr/share/container-scripts/postgresql/common.sh  
COPY ./s2i/bin/ $STI_SCRIPTS_PATH  
RUN chmod -Rf ug+rxw $STI_SCRIPTS_PATH && chown -Rf postgres:root
$STI_SCRIPTS_PATH  
RUN mkdir -p /opt/s2i/destination && chmod -R ug+rw /opt/s2i/destination &&
chown -R postgres:root /opt/s2i/destination  
  
#And end by making the user postgres again  
USER 26

