FROM docker.io/baseruntime/baseruntime:latest  
  
# Port on which will apache run  
EXPOSE 8080  
# Image metadata  
ENV NAME=perl \  
PERL_VERSION=5.24 \  
VERSION=0 \  
RELEASE=1 \  
ARCH=x86_64  
  
# Set labels used in OpenShift to describe the builder images  
LABEL com.redhat.component="$NAME" \  
name="$FGC/$NAME" \  
summary="Perl 5 is a highly capable, feature-rich programming language." \  
description="Perl 5 is a highly capable, feature-rich programming language
with over 29 years of development. Perl 5 runs on over 100 platforms." \  
version="$VERSION" \  
release="$RELEASE.$DISTTAG" \  
architecture="$ARCH" \  
usage="s2i build file:///your/app modularitycontainers/perl your-app" \  
io.k8s.description="Platform for building and running Perl 5.24 applications"
\  
io.k8s.display-name="Apache 2.4 with mod_perl/5.24" \  
io.openshift.expose-services="8080:http" \  
io.openshift.tags="builder,perl,perl524" \  
io.openshift.s2i.scripts-url=image:///usr/local/s2i  
  
COPY repos/* /etc/yum.repos.d/  
  
# Perl and build tools install + user addition  
RUN BUILD_TOOlS="bsdtar \  
findutils \  
gcc \  
make \  
gettext \  
tar \  
wget \  
python " && \  
microdnf install perl perl-devel && \  
microdnf --nodocs --enablerepo fedora install -y mod_perl cpan cpanminus httpd
\  
$BUILD_TOOlS && \  
microdnf clean all  
RUN mkdir -p /opt/app-root/src/ && \  
useradd -u 1002 -r -g 0 -d /opt/app-root/src -s /sbin/nologin \  
-c "Default Application User" default && \  
chown -R 1002:0 /opt/app-root  
  
# Copy s2i files  
COPY ./s2i/bin/ /usr/local/s2i  
  
# Copy apache configuration  
COPY ./contrib/ /opt/app-root  
  
# Drop the root user  
RUN mkdir -p /opt/app-root/etc/httpd.d && \  
sed -i -f /opt/app-root/etc/httpdconf.sed etc/httpd/conf/httpd.conf && \  
chmod -R og+rwx /var/run/httpd /opt/app-root/etc/httpd.d && \  
chown -R 1002:0 /opt/app-root && chmod -R ug+rwx /opt/app-root  
  
USER 1002  
# Copy executable utilities.  
COPY bin/ /usr/bin/  
  
# Copy help file  
COPY root/help.1 /  
  
# Directory with the sources is set as the working directory so all STI
scripts  
# can execute relative to this path.  
WORKDIR /opt/app-root/src  
  
# Set the default command to print the usage  
CMD /usr/local/s2i/usage

