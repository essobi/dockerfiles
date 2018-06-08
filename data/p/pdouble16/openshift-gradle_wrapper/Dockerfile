FROM pdouble16/openshift-s2i-browser-base:0.3  
MAINTAINER "Patrick Double <pat@patdouble.com>"  
ARG BUILD_DATE  
ARG SOURCE_COMMIT  
ARG DOCKERFILE_PATH  
ARG SOURCE_TYPE  
  
LABEL io.k8s.description="Builder for WAR files using the Gradle wrapper" \  
io.k8s.display-name="Gradle Wrapper" \  
io.openshift.expose-services="8080:http" \  
io.openshift.tags="builder,gradle,java" \  
io.openshift.min-memory="1Gi" \  
org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.docker.dockerfile="$DOCKERFILE_PATH/Dockerfile" \  
org.label-schema.license="GPLv2" \  
org.label-schema.name="Builder for WAR files using the Gradle wrapper" \  
org.label-schema.url="https://bitbucket.org/double16/openshift-gradle_wrapper"
\  
org.label-schema.vcs-ref=$SOURCE_COMMIT \  
org.label-schema.vcs-type="$SOURCE_TYPE" \  
org.label-schema.vcs-url="https://bitbucket.org/double16/openshift-
gradle_wrapper.git"  
  
USER root  
  
# Some proxies will get in the way here, so increasing to avoid time out
errors  
RUN echo "timeout=200" >> /etc/yum.conf  
RUN yum install -y java-1.8.0-openjdk-devel nc netstat nss_wrapper gettext &&
yum clean all -y  
  
# Install expected versions of Gradle  
ENV GRADLE_USER_HOME=/opt/gradle  
RUN mkdir -p ${GRADLE_USER_HOME}  
COPY ./gradle-wrapper-fetch ${GRADLE_USER_HOME}/gradle-wrapper-fetch  
RUN chown -R 1001 ${GRADLE_USER_HOME}  
USER 1001  
RUN ${GRADLE_USER_HOME}/gradle-wrapper-fetch/fetch-gradle-version.sh 2.14.1
bin && ${GRADLE_USER_HOME}/gradle-wrapper-fetch/fetch-gradle-version.sh 2.14.1
all  
RUN ${GRADLE_USER_HOME}/gradle-wrapper-fetch/fetch-gradle-version.sh 3.4.1 bin
&& ${GRADLE_USER_HOME}/gradle-wrapper-fetch/fetch-gradle-version.sh 3.4.1 all  
RUN ${GRADLE_USER_HOME}/gradle-wrapper-fetch/fetch-gradle-version.sh 3.5 bin
&& ${GRADLE_USER_HOME}/gradle-wrapper-fetch/fetch-gradle-version.sh 3.5 all  
  
# Install S2I scripts  
USER root  
LABEL io.openshift.s2i.scripts-url=image:///usr/libexec/s2i  
COPY ./s2i/bin/ /usr/libexec/s2i  
RUN chmod a+x /usr/libexec/s2i/*  
  
# Copy password template  
COPY ./passwd.template /opt/  
  
USER 1001  
EXPOSE 8080  
CMD ["/usr/libexec/s2i/usage"]  

