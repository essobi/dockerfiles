FROM openjdk:8-slim  
  
LABEL maintainer="Pietrangelo Masala <p.masala@entando.com>"  
  
# TODO: Rename the builder environment variable to inform users about
application you provide them  
ENV ENTANDO_BASE_IMAGE_MORTGAGE_DEMO=1.0  
ENV JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64  
ENV JRE_HOME=/usr/lib/jvm/java-8-openjdk-amd64/jre  
ENV MAVEN_HOME=/usr/share/maven  
  
# TODO: Set labels used in OpenShift to describe the builder image  
LABEL io.k8s.description="Entando base image for the mortgage demo" \  
io.k8s.display-name="Entando base image mortgage-demo 1.0" \  
io.openshift.tags="mortgage,entando,bpms."  
  
# TODO: Install required packages here: and create the directory where the
project will run  
# /opt/entando, Make the user 1001 owner of this directory  
RUN apt-get update && apt-get install --no-install-recommends -y maven
imagemagick git \  
&& apt-get autoclean -y \  
&& mkdir -p /opt/entando && mkdir -p /opt/entando/.m2/repository && chown -R
1001:1001 /opt/entando && chmod 0777 -R /opt/entando  
  
# This default user  
USER 1001  
  
# Install entando dependencies (core, components, components-enterprise,
archetypes)  
RUN cd /opt/entando \  
&& git clone https://github.com/entando/mortgage.git \  
&& cd mortgage/entando-core \  
&& mvn -Dmaven.repo.local=/opt/entando/.m2/repository install -DskipTests &&
mvn clean && cd .. \  
&& cd entando-components \  
&& mvn -Dmaven.repo.local=/opt/entando/.m2/repository install -DskipTests &&
mvn clean && cd .. \  
&& cd entando-archetypes \  
&& mvn -Dmaven.repo.local=/opt/entando/.m2/reposistory install -DskipTests &&
mvn clean && cd .. \  
&& cd entando-components-enterprise \  
&& mvn -Dmaven.repo.local=/opt/entando/.m2/repository install -DskipTests &&
mvn clean && cd .. \  
&& cd .. && rm -rf mortgage/ \  
&& chmod 777 -R /opt/entando/.m2/repository/  

