FROM kiyoto/fluentd:0.10.56-2.1.1  
MAINTAINER kiyoto@treausure-data.com  
RUN mkdir /etc/fluent  
  
RUN apt-get update && apt-get install --yes make libcurl4-gnutls-dev && apt-
get clean all  
  
RUN ["/usr/local/bin/gem", "install", "fluent-plugin-record-reformer", "--no-
rdoc", "--no-ri"]  
RUN ["/usr/local/bin/gem", "install", "fluent-plugin-elasticsearch", "--no-
rdoc", "--no-ri"]  
RUN ["/usr/local/bin/gem", "install", "fluent-plugin-kubernetes", "--no-rdoc",
"--no-ri"]  
  
ADD fluent.conf /etc/fluent/  
ADD fluent-kubernetes.conf /etc/fluent/  
ADD run.sh /run.sh  
  
ENTRYPOINT ["/run.sh"]  
  

