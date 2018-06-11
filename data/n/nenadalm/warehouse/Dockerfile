FROM openshift/base-centos7  
  
ENV LEIN_ROOT=1  
RUN curl -L
https://copr.fedorainfracloud.org/coprs/nenadalm/phantomjs/repo/epel-7/nenadalm-
phantomjs-epel-7.repo -o /etc/yum.repos.d/nenadalm-phantomjs.repo  
  
RUN yum install -y --setopt=tsflags=nodocs \  
  
# leiningen deps  
java-1.8.0-openjdk \  
  
phantomjs \  
  
yum clean all -y && \  
  
# leiningen  
curl -L https://raw.githubusercontent.com/technomancy/leiningen/2.7.1/bin/lein
-o /usr/local/bin/lein && \  
chmod +x /usr/local/bin/lein  
  
COPY s2i/bin /usr/libexec/s2i  
  
EXPOSE 3000  
USER 1001  

