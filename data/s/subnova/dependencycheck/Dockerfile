FROM openjdk:8 AS build-env  
RUN apt-get update && \  
apt-get install -y --no-install-recommends wget ruby curl apt-transport-https
gpg && \  
curl https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor \  
> /etc/apt/trusted.gpg.d/microsoft.gpg && \  
echo "deb [arch=amd64] https://packages.microsoft.com/repos/microsoft-debian-
stretch-prod stretch main" \  
> /etc/apt/sources.list.d/dotnetdev.list && \  
apt-get update && \  
apt-get install -y --no-install-recommends dotnet-runtime-2.0.6  
  
RUN wget http://apache.claz.org/maven/maven-3/3.5.2/binaries/apache-
maven-3.5.2-bin.tar.gz && \  
tar -zxvf apache-maven-3.5.2-bin.tar.gz && \  
mv apache-maven-3.5.2 /opt/maven  
  
RUN mkdir data  
WORKDIR data  
COPY pom.xml pom.xml  
COPY ant/ ant/  
COPY archetype/ archetype/  
COPY build-reporting/ build-reporting/  
COPY cli/ cli/  
COPY core/ core/  
COPY maven/ maven/  
COPY src/ src/  
COPY utils/ utils/  
  
RUN /opt/maven/bin/mvn package  
  
RUN unzip -l cli/target/dependency-check-3.1.2-SNAPSHOT-release.zip  
  
FROM openjdk:8-jre-slim  
  
MAINTAINER Timo Pagel <dependencycheckmaintainer@timo-pagel.de>  
  
ENV user=dependencycheck  
  
COPY \--from=build-env /data/cli/target/dependency-check-3.1.2-SNAPSHOT-
release.zip .  
  
RUN apt-get update && \  
apt-get install -y --no-install-recommends wget ruby curl apt-transport-https
gpg && \  
gem install bundle-audit && \  
gem cleanup && \  
curl https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor \  
> /etc/apt/trusted.gpg.d/microsoft.gpg && \  
echo "deb [arch=amd64] https://packages.microsoft.com/repos/microsoft-debian-
stretch-prod stretch main" \  
> /etc/apt/sources.list.d/dotnetdev.list && \  
apt-get update && \  
apt-get install -y --no-install-recommends dotnet-runtime-2.0.6  
  
RUN file="dependency-check-3.1.2-SNAPSHOT-release.zip" && \  
unzip ${file} && \  
rm ${file} && \  
mv dependency-check /usr/share/ && \  
useradd -ms /bin/bash ${user} && \  
chown -R ${user}:${user} /usr/share/dependency-check && \  
mkdir /report && \  
chown -R ${user}:${user} /report && \  
apt-get remove --purge -y wget curl gpg && \  
apt-get autoremove -y && \  
rm -rf /var/lib/apt/lists/* /tmp/*  
  
VOLUME ["/src" "/usr/share/dependency-check/data" "/report"]  
  
WORKDIR /src  
  
CMD ["--help"]  
ENTRYPOINT ["/usr/share/dependency-check/bin/dependency-check.sh"]  

