FROM dexterbt1/sbt-0.11.2-docker  
  
MAINTAINER Dexter Tad-y <dtady@cpan.org>  
  
RUN apt-get update && apt-get install -y procps vim unzip git  
  
ENV JAVA_HOME /usr/lib/jvm/java-7-oracle  
  
RUN useradd -m mq  
  
ENV KESTREL_GITUSER dexterbt1  
ENV KESTREL_GITPROJ kestrel  
ENV KESTREL_GITHASH 199063ed7d362aa25d136e48e3b8237c459483e8  
  
RUN cd /home/mq; \  
su mq -c "mkdir tmp"; \  
cd tmp; \  
su mq -c "wget -c
https://github.com/${KESTREL_GITUSER}/${KESTREL_GITPROJ}/archive/${KESTREL_GITHASH}.zip";
\  
su mq -c "unzip ${KESTREL_GITHASH}.zip"  
  
RUN cd /home/mq/tmp/${KESTREL_GITPROJ}-${KESTREL_GITHASH}; \  
sbt clean  
  
RUN mkdir -p /root/.m2/repository/org/scala-tools/testing/specs_2.9.2/  
  
ADD specs_2.9.2__1.6.9 /root/.m2/repository/org/scala-
tools/testing/specs_2.9.2/1.6.9  
  
RUN cd /home/mq/tmp/${KESTREL_GITPROJ}-${KESTREL_GITHASH}; \  
sbt package-dist  
  
VOLUME ["/var/log/kestrel", "/var/run/kestrel"]  
  
RUN mkdir -p /usr/local/kestrel; \  
cd /usr/local/kestrel; \  
ln -s /home/mq/tmp/${KESTREL_GITPROJ}-${KESTREL_GITHASH}/dist/kestrel current;  
  

