FROM ubuntu:14.04.4  
MAINTAINER Dmitry Mozzherin  
ENV LAST_FULL_REBUILD 2016-06-29  
ARG VERSION="0.1.0-SNAPSHOT"  
RUN apt-get update \  
&& apt-get install -y apt-transport-https apt-utils \  
software-properties-common \  
&& apt-add-repository ppa:brightbox/ruby-ng \  
&& apt-add-repository ppa:openjdk-r/ppa \  
&& apt-get update \  
&& apt-get install -y ruby2.3 ruby2.3-dev ruby-switch \  
libxslt-dev supervisor build-essential nodejs supervisor \  
zlib1g-dev libssl-dev libreadline-dev libyaml-dev \  
libxml2-dev libxslt-dev nodejs libpq-dev liblzma-dev \  
openjdk-8-jre curl postgresql-client \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN locale-gen en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8  
RUN ruby-switch --set ruby2.3  
RUN echo 'gem: --no-rdoc --no-ri' | tee -a $HOME/.gemrc  
RUN gem install bundle  
  
RUN mkdir /app  
WORKDIR /app  
  
ENV ASSEMBLY_JAR "gnresolver-api-assembly-${VERSION}.jar"  
ENV ASSEMBLY_PATH
"https://github.com/GlobalNamesArchitecture/gnresolver/releases/download/snapshot/${ASSEMBLY_JAR}"  
ADD ${ASSEMBLY_PATH} /app/  
#RUN chmod 777 "/app/${ASSEMBLY_JAR}"  
#ARG ASSEMBLY_NAME  
#USER root  
CMD bash -c "java -jar ${ASSEMBLY_JAR}"  
  
#CMD ["java", "-server", "-Xms4g", "-Xmx8g", "-XX:PermSize=512m",
"-XX:MaxPermSize=512m",  
# "-XX:+UseConcMarkSweepGC", "-XX:+CMSParallelRemarkEnabled",  
# "-XX:+UseCMSInitiatingOccupancyOnly",
"-XX:CMSInitiatingOccupancyFraction=70",  
# "-XX:+ScavengeBeforeFullGC", "-XX:+CMSScavengeBeforeRemark",  
# "-XX:+HeapDumpOnOutOfMemoryError", "-XX:HeapDumpPath=dump-`date`.hprof"]  

