FROM python:3.6.1  
RUN apt-get update \  
&& apt-get install unzip \  
&& apt-get install -y postgresql postgresql-contrib \  
&& apt-get install sudo \  
&& wget -O /tmp/apache-tinkerpop-gremlin-server-3.2.4-bin.zip
"http://mirror.fibergrid.in/apache/tinkerpop/3.2.4/apache-tinkerpop-gremlin-
server-3.2.4-bin.zip" \  
&& unzip /tmp/apache-tinkerpop-gremlin-server-3.2.4-bin.zip -d / \  
&& wget -O /tmp/java.tar.gz
"http://javadl.oracle.com/webapps/download/AutoDL?BundleId=220305_d54c1d3a095b4ff2b6607d096fa80163"
\  
&& cd /tmp/ \  
&& tar zxvf java.tar.gz \  
&& mv ./jre1.8.0_131 /jre1.8.0_131 \  
&& ln -s /jre1.8.0_131/bin/java /usr/local/bin/java \  
&& cd /apache-tinkerpop-gremlin-server-3.2.4 \  
&& bin/gremlin-server.sh -i org.apache.tinkerpop gremlin-python 3.2.4 \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# script to start gremlin server for bitbucket pipeline  
RUN printf '#!/bin/bash\ncd /apache-tinkerpop-gremlin-server-3.2.4\nnohup
bin/gremlin-server.sh conf/gremlin-server-modern-py.yaml > /dev/null 2>&1
&\nexec "$@"' > /start.sh \  
&& chmod 777 /start.sh  
  
RUN apt-get update \  
&& apt-get install -y openssh-server  
  
EXPOSE 8182  
ADD files /  
RUN chmod 700 /default_cmd  
CMD ["/default_cmd"]  
  

