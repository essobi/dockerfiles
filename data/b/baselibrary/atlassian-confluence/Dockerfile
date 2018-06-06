FROM baselibrary/java:8  
MAINTAINER ShawnMa <qsma@thoughtworks.com>  
  
## Version  
ENV CONFLUENCE_MAJOR 5  
ENV CONFLUENCE_VERSION 5.9.10  
## Packages  
RUN \  
mkdir -p /opt/atlassian &&\  
curl -fsSL
"http://confluence.goldpitcher.co.kr/download/attachments/166564194/atlassian-
confluence-${CONFLUENCE_VERSION}.tar.gz"| tar -zxvf - --strip-components=1 -C
/opt/atlassian  
  
## Configurations  
RUN \  
mkdir -p /var/lib/atlassian &&\  
echo "confluence.home=/var/lib/confluence" > "/opt/atlassian/confluence/WEB-
INF/classes/confluence-init.properties"  
  
EXPOSE 8090  
WORKDIR /var/lib/confluence  
  
VOLUME ["/var/lib/confluence"]  
  
CMD ["/opt/atlassian/bin/catalina.sh", "run"]

