FROM jetty  
MAINTAINER Cam Morris <cam.morris@owasp.org>  
ARG VERSION=0.8.3  
ENV PASSFAULT_WORDLISTS=${JETTY_BASE}/webapps/ROOT/WEB-
INF/classes/org/owasp/passfault/wordlists  
ENV PASSFAULT_POLICY=${JETTY_BASE}/webapps/ROOT/policy.json  
  
ADD
https://github.com/owasp/passfault/releases/download/v${VERSION}/passfault-
jsonService-${VERSION}.war /tmp/passfault.war  
RUN mkdir ${JETTY_BASE}/webapps/ROOT && \  
unzip /tmp/passfault.war -d ${JETTY_BASE}/webapps/ROOT && \  
chown -R jetty:jetty ${JETTY_BASE}/webapps/ROOT && \  
rm /tmp/passfault.war  
  
ONBUILD RUN chown -R jetty:jetty ${JETTY_BASE}/webapps/ROOT  

