#docker build -f Dockerfile -t openweb/hippo-repository-checker .  
FROM java:8-jre  
MAINTAINER Joost Oudeman <joost@openweb.nl>  
  
ENV ENCODING=UTF-8 \  
CHECKER_HOME=/usr/local/hippo-addon/checker \  
  
MAX_HEAP=1024 \  
MIN_HEAP=256 \  
EXTRA_JVM_OPTS= \  
  
DB_HOST="mysql" \  
DB_PORT=3306 \  
DB_NAME=hippo \  
DB_USER=hippo \  
DB_PASS=""  
# Add Hippo's Checker repository maintenance tool  
RUN mkdir -p /usr/local/hippo-addon/checker &&\  
cd /usr/local/hippo-addon/checker &&\  
wget -O hippo-addon-checker.jar
http://maven.onehippo.com/maven2/org/onehippo/cms7/hippo-addon-
checker/1.02.04/hippo-addon-checker-1.02.04.jar  
  
WORKDIR $CHECKER_HOME  
  
COPY conf/repository.xml checker-repository.xml.template  
  
COPY bin/wait-for-it.sh /usr/local/bin/wait-for-it.sh  
COPY bin/entrypoint.sh /usr/local/bin/entrypoint.sh  
COPY bin/setenv.sh /usr/local/bin/setenv.sh  
COPY bin/checker.sh /usr/local/bin/checker.sh  
  
RUN chmod +x /usr/local/bin/*.sh  
  
VOLUME ["/usr/local/hippo-addon/checker/storage"]  
  
ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]  
  
CMD ["checker.sh"]

