FROM docker.elastic.co/kibana/kibana:6.2.3  
  
USER root  
  
RUN yum update -y && \  
yum install -y epel-release && \  
yum install -y dpkg && \  
/usr/share/kibana/bin/kibana-plugin install
https://oss.sonatype.org/content/repositories/releases/com/floragunn/search-
guard-kibana-plugin/6.2.3-11/search-guard-kibana-plugin-6.2.3-11.zip && \  
chown -R kibana:kibana /usr/share/kibana/config
/usr/share/kibana/plugins/searchguard /usr/share/kibana/optimize/bundles && \  
# install gosu  
dpkgArch="$(dpkg --print-architecture | awk -F- '{ print $NF }')" && \  
curl -fsSL
"https://github.com/tianon/gosu/releases/download/1.10/gosu-$dpkgArch" -o
/usr/local/bin/gosu && \  
chmod +x /usr/local/bin/gosu && \  
gosu nobody true && \  
# complete gosu  
yum remove -y dpkg && yum clean all -y  
  
CMD ["gosu", "kibana", "/usr/local/bin/kibana-docker"]  

