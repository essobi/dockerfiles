# A simple Dockerized http server written in Akka + Spray (spray-can)
framework  
#  
# URL: https://github.com/William-Yeh/docker-spray-httpserver  
#  
# Reference:  
# - http://spray.io/documentation/1.1-SNAPSHOT/spray-can/examples/#simple-
http-server  
#  
# Version 0.1  
#  
# pull base image  
FROM williamyeh/scala:2.11.4  
MAINTAINER William Yeh <william.pjyeh@gmail.com>  
  
  
RUN apt-get update && \  
echo "==> Install git & helper tools..." && \  
DEBIAN_FRONTEND=noninteractive \  
apt-get install -y -q --no-install-recommends git && \  
\  
\  
\  
echo "==> Download source..." && \  
cd /tmp && \  
git clone https://github.com/spray/spray.git && \  
cd spray && \  
\  
\  
\  
echo "==> Download patch..." && \  
wget -N \  
-P project \  
https://gist.githubusercontent.com/William-
Yeh/dd6316b8f93175ab80c7/raw/04884aa7b81f6f06a873017a44a7143922d6b7fc/plugins.sbt
&& \  
wget -N \  
-P project \  
https://gist.githubusercontent.com/William-
Yeh/dd6316b8f93175ab80c7/raw/29bd3840f1f94aed70483b54ff10a48530974509/Build.scala
&& \  
wget -N \  
-P examples/spray-can/simple-http-server/src/main/scala/spray/examples \  
https://gist.githubusercontent.com/William-
Yeh/dd6316b8f93175ab80c7/raw/72d6ce12bca6c8f6b707d8ae6082b3efe9b0fbe7/Main.scala
&& \  
wget -N \  
-P examples/spray-can/simple-http-server/src/main/scala/spray/examples \  
https://gist.githubusercontent.com/William-
Yeh/dd6316b8f93175ab80c7/raw/0826724b9f6842a443307353e5ab48c1602643b7/DemoService.scala
&& \  
\  
\  
\  
echo "==> Compile & package..." && \  
sbt "project simple-http-server" assembly && \  
mv examples/spray-can/simple-http-server/target/scala-2.10/simple-http-server-
assembly-1.1-SNAPSHOT.jar /opt/simple-http-server.jar && \  
\  
\  
\  
echo "==> Clean up..." && \  
cd /tmp && \  
rm -rf spray && \  
apt-get remove -y --auto-remove git && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
# configure  
# HTTP port  
EXPOSE 8080  
# for convenience  
RUN date '+%Y-%m-%dT%H:%M:%S%:z' > /var/log/DOCKER_BUILD_TIME  
  
# Define default command.  
ENTRYPOINT ["java", "-jar", "/opt/simple-http-server.jar"]  
CMD ["-XX:+UseG1GC"]  

