#  
# WSO2 ESB 4.9.0 on CentOS Linux with Oracle JDK 1.7.0_80  
#  
FROM thoeni/wso2esb:4.9.0  
MAINTAINER Antonio Troina, thoeni@gmail.com  
  
ENV WSO2_SOFT_VER=4.9.0  
# copy zip from local folder to container  
RUN sed -i.bak '/<StatisticsReporterDisabled>/ s/true/false/'
/opt/wso2esb/repository/conf/carbon.xml && \  
sed -i.bak '/<parameter name="cachableDuration">/ s/15000/1000/'
/opt/wso2esb/repository/deployment/server/synapse-configs/default/registry.xml
&& \  
echo -e
"<BamConfig>\n\t<ServiceDataPublishing>enable</ServiceDataPublishing>\n\t<WebappDataPublishing>disable</WebappDataPublishing>\n</BamConfig>"
> /opt/wso2esb/repository/conf/etc/bam.xml  
  
CMD ["/opt/wso2esb/bin/wso2server.sh"]  

