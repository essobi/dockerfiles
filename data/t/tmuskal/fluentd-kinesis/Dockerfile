FROM kiyoto/fluentd:0.10.56-2.1.1  
MAINTAINER tal@musk.al  
  
RUN mkdir /etc/fluent  
  
ADD fluent.conf /etc/fluent/  
  
RUN ["/usr/local/bin/gem", "install", "fluent-plugin-record-reformer", "--no-
rdoc", "--no-ri"]  
  
RUN ["/usr/local/bin/gem", "install", "fluent-plugin-forest", "--no-rdoc", "--
no-ri"]  
  
RUN ["/usr/local/bin/gem", "install", "fluent-plugin-kinesis", "--no-rdoc", "
--no-ri"]  
  
ENTRYPOINT ["/usr/local/bin/fluentd", "-c", "/etc/fluent/fluent.conf","--
use-v1-config"]

