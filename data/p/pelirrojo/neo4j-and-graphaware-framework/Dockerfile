FROM openjdk:8-jre-alpine  
  
maintainer Linonetwo, linonetwo012@gmail.com  
  
## from offical Dockerfile  
  
RUN apk add --no-cache --quiet \  
bash \  
curl  
  
ENV NEO4J_SHA256
f0d79b4a98672dc527b708113644b8961ba824668c354e61dc4d2a16d8484880  
ENV NEO4J_TARBALL neo4j-community-3.1.3-unix.tar.gz  
ARG NEO4J_URI=http://dist.neo4j.org/neo4j-community-3.1.3-unix.tar.gz  
  
RUN curl --fail --silent --show-error --location --remote-name ${NEO4J_URI} \  
&& echo "${NEO4J_SHA256} ${NEO4J_TARBALL}" | sha256sum -csw - \  
&& tar --extract --file ${NEO4J_TARBALL} --directory /var/lib \  
&& mv /var/lib/neo4j-* /var/lib/neo4j \  
&& rm ${NEO4J_TARBALL}  
  
## add graphaware  
  
  
WORKDIR /var/lib/neo4j/plugins  
RUN apk update && \  
apk add ca-certificates wget && \  
update-ca-certificates && \  
wget https://products.graphaware.com/download/framework-server-
community/graphaware-server-community-all-3.1.3.46.jar && \  
wget https://products.graphaware.com/download/timetree/graphaware-
timetree-3.1.3.45.26.jar && \  
wget https://products.graphaware.com/download/uuid/graphaware-
uuid-3.1.3.45.14.jar  
  
## from offical Dockerfile  
  
WORKDIR /var/lib/neo4j  
  
RUN mv data /data \  
&& ln -s /data  
  
VOLUME /data  
  
COPY launch.sh /launch.sh  
  
## enable graphaware framework  
  
COPY neo4j.addition.conf conf/neo4j.addition.conf  
RUN cat conf/neo4j.addition.conf >> conf/neo4j.conf  
  
## export port and start, where launch.sh is from offical repo  
  
EXPOSE 7474 7473 7687  
  
ENTRYPOINT ["/launch.sh"]  
CMD ["neo4j"]  

