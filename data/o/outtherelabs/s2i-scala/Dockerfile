# scala  
FROM centos/s2i-base-centos7  
  
MAINTAINER Patrick Tescher <patrick@outtherelabs.com>  
  
# Labels used in OpenShift to describe the builder image  
LABEL summary="Platform for building and running Scala applications in Java 8"
\  
io.k8s.description="Platform for building and running Scala applications in
Java 8" \  
io.k8s.display-name="Scala with Java 8" \  
io.openshift.expose-services="9000:http,8778:jolokia" \  
io.openshift.tags="builder,scala,java8" \  
com.redhat.dev-mode="DEV_MODE:false" \  
com.redhat.deployments-dir="/opt/app-root/src" \  
com.redhat.dev-mode.port="DEBUG_PORT:5005"  
  
# Install Java, SBT, and openshift client  
RUN yum update -y && \  
yum install -y java-1.8.0-openjdk-devel && \  
curl https://bintray.com/sbt/rpm/rpm | tee /etc/yum.repos.d/bintray-sbt-
rpm.repo && \  
yum install -y sbt && \  
set -o pipefail && curl -L
https://github.com/openshift/origin/releases/download/v3.6.0/openshift-origin-
client-tools-v3.6.0-c4dd4cf-linux-64bit.tar.gz | \  
tar -zx && \  
mv openshift*/oc /usr/local/bin && \  
rm -rf openshift-origin-client-tools-*  
  
# Copy test app to cache directory  
COPY ./test/test-app /opt/test-app-root  
  
# Cache SBT dependencies and plugins from test app  
RUN cd /opt/test-app-root && \  
./sbt \  
-ivy /opt/app-root/src/.ivy2 \  
-sbt-dir /opt/app-root/src/.sbt \  
-sbt-boot /opt/app-root/src/.sbt/boot \  
compile && \  
rm -rf /opt/test-app-root && \  
chown -R 1001:0 /opt/app-root && chmod -R ug+rwx /opt/app-root  
  
# Copy the S2I scripts from the specific language image to $STI_SCRIPTS_PATH  
COPY s2i/bin/ $STI_SCRIPTS_PATH  
  
# Make sure we are running as user 1001  
USER 1001  
# Expose default Play and Jolokia ports  
EXPOSE 9000 8778  
# Set the default CMD for the image  
CMD $STI_SCRIPTS_PATH/usage  

