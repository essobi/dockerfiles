FROM openjdk:8  
RUN apt-get update \  
&& apt-get install -y maven scala  
COPY . /src  
RUN cd /src && ./gradlew clean jar -x test  
  
FROM openjdk:8-jre-slim  
COPY run.sh /run.sh  
WORKDIR /  
COPY \--from=0 /src/kafka*jar /  
RUN apt-get update \  
&& apt-get install -y gnupg \  
&& apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv E56151BF \  
&& echo "deb http://repos.mesosphere.com/debian stretch main" | tee -a
/etc/apt/sources.list.d/mesosphere.list \  
&& apt-get update \  
&& apt-get install -y libcurl4-nss-dev libsasl2-modules libsvn1 libevent-dev
libcurl3 curl iproute2 \  
&& apt-get download mesos=1.5.0\\* \  
&& dpkg --unpack mesos*.deb \  
&& rm /var/lib/dpkg/info/mesos.postinst -f \  
&& dpkg --configure mesos \  
&& rm -f /mesos*deb \  
&& curl -sLO https://archive.apache.org/dist/kafka/1.1.0/kafka_2.11-1.1.0.tgz  
ENTRYPOINT ["/run.sh"]  

