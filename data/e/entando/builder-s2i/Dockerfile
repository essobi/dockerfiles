  
# entando-builder  
FROM centos:7  
MAINTAINER Pietrangelo Masala <p.masala@entando.com>  
  
### Atomic/OpenShift Labels  
LABEL name="entando/entando-builder-s2i" \  
maintainer="Pietrangelo Masala <p.masala@entando.com>" \  
vendor="Entando Srl" \  
version="1" \  
release="1" \  
summary="Entando base image for running on OpenShift environments" \  
description="This base image let you deploy your entando project on OpenShift"
\  
url="https://www.entando.com" \  
run='docker run -ti --rm --name ${NAME} \  
-u 123456 \  
${IMAGE}' \  
io.k8s.description="Entando base image for running on OpenShift environments"
\  
io.k8s.display-name="Entando base image 1.1" \  
io.openshift.expose-services="8080:http" \  
io.openshift.tags="entando,ux,openshift,docker" \  
io.openshift.s2i.scripts-url=image:///usr/local/s2i  
  
#Environment Variables  
ENV JAVA_HOME=/usr/lib/jvm/java-1.8.0  
ENV JRE_HOME=/usr/lib/jvm/jre-1.8.0  
ENV MAVEN_HOME=/usr/share/maven  
ENV MAVEN_LOCAL_REPO=/opt/entando/.m2/repository  
ENV MAVEN_RELEASE=3.5.3  
ENV APP_ROOT=/opt/entando  
ENV PATH=${APP_ROOT}/bin:${PATH}  
ENV HOME=${APP_ROOT}  
  
#COPY bin/ ${APP_ROOT}/bin/  
# Copy maven settings.xml to overwrite default one  
COPY settings.xml /tmp/settings.xml  
# sets io.openshift.s2i.scripts-url label that way, or update that label  
COPY ./s2i/bin/ /usr/local/s2i  
  
# Install Entando dependencies, software requirements and users  
RUN adduser --system -u 10001 10001 \  
&& yum -y install git java-1.8.0-openjdk-devel ImageMagick git wget \  
&& mkdir -p ${APP_ROOT} && mkdir -p ${MAVEN_LOCAL_REPO} \  
&& chown 10001:0 /etc/passwd && chmod ug+w /etc/passwd \  
&& cd /tmp && wget
http://www.eu.apache.org/dist/maven/maven-3/${MAVEN_RELEASE}/binaries/apache-
maven-${MAVEN_RELEASE}-bin.tar.gz \  
&& tar xzf apache-maven-${MAVEN_RELEASE}-bin.tar.gz \  
&& mkdir ${MAVEN_HOME} \  
&& cd apache-maven-${MAVEN_RELEASE}/ && cp -R * ${MAVEN_HOME} && cd .. && rm
-rf /tmp/apache-maven* \  
&& alternatives --install /usr/bin/mvn mvn ${MAVEN_HOME}/bin/mvn 1 \  
&& alternatives --auto mvn \  
&& rm -f ${MAVEN_HOME}/conf/settings.xml \  
&& cp /tmp/settings.xml ${MAVEN_HOME}/conf/settings.xml \  
&& cd ${APP_ROOT} \  
&& git clone https://github.com/entando/entando-archetypes.git \  
&& cd entando-archetypes && mvn -Dmaven.repo.local=${MVN_LOCAL_REPO} install
&& cd .. \  
&& rm -rf entando-* \  
&& chgrp -R 0 ${APP_ROOT}/ && chown -R 10001:0 ${APP_ROOT}/ && chmod -R ug+w
${APP_ROOT}/ \  
&& yum -y clean all  
  
# run as user 10001 for OpenShift security constraints  
USER 10001  
WORKDIR ${APP_ROOT}  
  
EXPOSE 8080  
CMD ["/usr/local/s2i/usage"]

