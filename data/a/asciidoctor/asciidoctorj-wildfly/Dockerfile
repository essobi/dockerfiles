FROM jboss/wildfly:8.2.0.Final  
MAINTAINER Maxime Gréau <greau.maxime@gmail.com>  
  
# Create a WildFly admin user to deploy app with CLI  
RUN /opt/jboss/wildfly/bin/add-user.sh -up mgmt-users.properties admin
Admin#70365 --silent  
  
# Set env variables for versions  
ENV ASCIIDOCTORJ_VERSION 1.5.2  
ENV ASCIIDOCTORJ_PDF_VERSION 1.5.0-alpha.6  
ENV ASCIIDOCTORJ_EPUB3_VERSION 1.5.0-alpha.4  
ENV JRUBY_VERSION 1.7.16.1  
# Handle asciidoctor-backends  
ENV ASCIIDOCTOR_BACKENDS /opt/jboss/asciidoctor-backends  
RUN mkdir -p ${ASCIIDOCTOR_BACKENDS}  
  
# Create the AsciidoctorJ module  
RUN mkdir -p ${JBOSS_HOME}/modules/org/asciidoctor/main  
ENV ASCIIDOCTORJ_MODULE /opt/jboss/wildfly/modules/org/asciidoctor/main  
  
# Output directory to store generated files  
ENV OUTPUT_DIRECTORY /tmp/documents  
RUN mkdir -p ${OUTPUT_DIRECTORY}  
  
# Set the ULR_BASE env variable to download artifacts  
ENV URL_BASE https://repo1.maven.org/maven2/  
  
ADD module.xml ${ASCIIDOCTORJ_MODULE}/module.xml  
  
RUN cd ${ASCIIDOCTORJ_MODULE} \  
&& curl -O
${URL_BASE}org/asciidoctor/asciidoctorj/${ASCIIDOCTORJ_VERSION}/asciidoctorj-${ASCIIDOCTORJ_VERSION}.jar
\  
&& curl -O ${URL_BASE}org/asciidoctor/asciidoctorj-
pdf/${ASCIIDOCTORJ_PDF_VERSION}/asciidoctorj-
pdf-${ASCIIDOCTORJ_PDF_VERSION}.jar \  
&& curl -O ${URL_BASE}org/asciidoctor/asciidoctorj-
epub3/${ASCIIDOCTORJ_EPUB3_VERSION}/asciidoctorj-
epub3-${ASCIIDOCTORJ_EPUB3_VERSION}.jar \  
&& curl -O -m 900 ${URL_BASE}org/jruby/jruby-complete/${JRUBY_VERSION}/jruby-
complete-${JRUBY_VERSION}.jar \  
\  
&& (curl -LkSs https://api.github.com/repos/asciidoctor/asciidoctor-
backends/tarball | tar xfz - -C ${ASCIIDOCTOR_BACKENDS} \--strip-components=1)  
  
WORKDIR ${OUTPUT_DIRECTORY}  
VOLUME ${OUTPUT_DIRECTORY}  
  
CMD ["/opt/jboss/wildfly/bin/standalone.sh", "-b", "0.0.0.0", "-bmanagement",
"0.0.0.0"]  

