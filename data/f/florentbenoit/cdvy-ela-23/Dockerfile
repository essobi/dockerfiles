FROM codenvy/ubuntu_jdk8  
RUN cd /tmp && git clone https://github.com/benoitf/elasticsearch && cd
elasticsearch && git checkout 2.3 && mvn clean install -am -pl dev-
tools,distribution/zip package -DskipTests && rm -rf
$HOME/.m2/repository/org/elasticsearch && rm -rf /tmp/elasticsearch  

