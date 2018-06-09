FROM kiyoto/fluentd:0.10.56-2.1.1  
MAINTAINER anton  
  
COPY fluent.conf /opt/fluent.conf  
RUN ["/usr/local/bin/gem", "install", "fluent-plugin-record-reformer", "--no-
rdoc", "--no-ri"]  
RUN ["/usr/local/bin/gem", "install", "fluent-plugin-forest", "--no-rdoc", "--
no-ri"]  
RUN ["/usr/local/bin/gem", "install", "fluent-plugin-s3", "--no-rdoc", "--no-
ri"]  
  
COPY startup-fluentd.sh /opt/startup-fluentd.sh  
CMD ["/opt/startup-fluentd.sh"]

