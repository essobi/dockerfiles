FROM sonatype/nexus3:3.12.0  
  
USER root  
  
ENV TZ=Australia/Melbourne  
  
COPY entrypoint.sh /  
  
RUN yum update -y && yum upgrade -y && yum install -y epel-release && yum
install -y tzdata dpkg && \  
# install gosu  
dpkgArch="$(dpkg --print-architecture | awk -F- '{ print $NF }')" && \  
curl -fsSL
"https://github.com/tianon/gosu/releases/download/1.10/gosu-$dpkgArch" -o
/usr/bin/gosu && \  
chmod +x /usr/bin/gosu && \  
gosu nobody true && \  
# complete gosu  
chmod +x /entrypoint.sh && \  
yum remove -y dpkg epel-release && yum clean all && rm -rf /var/cache/yum  
  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["gosu", "nexus", "bash", "-c", "${SONATYPE_DIR}/start-nexus-repository-
manager.sh"]  

