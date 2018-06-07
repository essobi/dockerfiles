FROM ubuntu:14.04.4 AS builder  
  
MAINTAINER Christian Oelsner <c.oelsner@web.de>  
  
WORKDIR /opt  
  
RUN apt-get update && apt-get install -y unzip  
  
ARG VERSION=1353  
# uncomment for local debugging  
# ADD ./terraria-server-${VERSION}.zip terraria-server.zip  
ADD http://terraria.org/server/terraria-server-${VERSION}.zip terraria-
server.zip  
  
RUN unzip terraria-server.zip "${VERSION}/Linux/*" \  
&& chmod -R a+rw ${VERSION}/Linux/* \  
&& chmod a+x ${VERSION}/Linux/TerrariaServer* \  
&& mv ${VERSION}/Linux terraria/  
  
# Stage 2  
FROM ubuntu:14.04.4  
WORKDIR /opt/terraria  
  
COPY \--from=builder /opt/terraria .  
  
VOLUME ["/world"]  
EXPOSE 7777  
ADD serverconfig.txt .  
  
ENTRYPOINT ./TerrariaServer -x64 -config serverconfig.txt  

