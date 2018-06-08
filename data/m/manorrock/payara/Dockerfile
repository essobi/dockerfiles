FROM manorrock/openjdk:8u161  
RUN zypper rr
http://download.opensuse.org/repositories/Java:/Factory/openSUSE_Tumbleweed/
&& \  
zypper --non-interactive refresh && \  
zypper --non-interactive install curl && \  
curl -O https://repo.maven.apache.org/maven2/fish/payara/extras/payara-
micro/5.181/payara-micro-5.181.jar && \  
mkdir -p /usr/local/payara/deployments && \  
mv payara-micro-5.181.jar /usr/local/payara/payara-micro.jar && \  
zypper --non-interactive remove curl && \  
zypper --non-interactive clean -a  
CMD ["java", "-jar", "/usr/local/payara/payara-micro.jar", "--deploymentDir",
"/usr/local/payara/deployments"]  
WORKDIR /mnt  

