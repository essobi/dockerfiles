FROM sonatype/nexus3:3.3.2  
USER root  
RUN yum install unzip cronie -y  
RUN echo "* * * * * df | grep '/nexus-data' | awk '{print \$2}' >
/metrics/nexus_data_volume_overall_size" > crontab.tmp \  
&& echo "* * * * * df | grep '/nexus-data' | awk '{print \$3}' >
/metrics/nexus_data_volume_used" >> crontab.tmp \  
&& crontab crontab.tmp \  
&& rm -rf crontab.tmp  
RUN mkdir -p /opt/sonatype/nexus/system/com/larscheidschmitzhermes/  
ADD https://github.com/larscheid-schmitzhermes/nexus3-github-oauth-
plugin/releases/download/1.1.0/nexus3-github-oauth-plugin.zip
/opt/sonatype/nexus/system/com/larscheidschmitzhermes/nexus3-github-oauth-
plugin.zip  
RUN unzip /opt/sonatype/nexus/system/com/larscheidschmitzhermes/nexus3-github-
oauth-plugin.zip -d /opt/sonatype/nexus/system/com/larscheidschmitzhermes/ &&
echo "mvn\:com.larscheidschmitzhermes/nexus3-github-oauth-plugin/1.1.0 = 200"
>> /opt/sonatype/nexus/etc/karaf/startup.properties  
WORKDIR /opt/sonatype/nexus  
ADD entrypoint.sh entrypoint.sh  
RUN chmod +x entrypoint.sh  
ENTRYPOINT ./entrypoint.sh

