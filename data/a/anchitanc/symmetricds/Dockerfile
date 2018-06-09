#To Build with specific Version :- docker build --build-arg
SYMMETRICDS_MAJOR_VERSION=3.9 SYMMETRICDS_MINOR_VERSION=2 -t sym .  
#To Build with default Version :- docker build -t sym .  
#docker run -it -v ./engines:/opt/symmetric-ds/engines -p 31415:31415 sym  
FROM openjdk:8-jre-alpine  
  
ARG SYMMETRICDS_MAJOR_VERSION=3.9  
ARG SYMMETRICDS_MINOR_VERSION=2  
ENV SYMMETRICDS_VERSION
${SYMMETRICDS_MAJOR_VERSION}.${SYMMETRICDS_MINOR_VERSION}  
ENV SYMMETRICDS_HOME /opt/symmetric-ds  
  
#RUN adduser -D symmetricds  
#COPY ./target.zip /symmetric-server-${SYMMETRICDS_VERSION}.zip  
RUN mkdir -p ${SYMMETRICDS_HOME} && \  
wget
https://sourceforge.net/projects/symmetricds/files/symmetricds/symmetricds-$SYMMETRICDS_MAJOR_VERSION/symmetric-
server-$SYMMETRICDS_VERSION.zip/download -O symmetric-
server-$SYMMETRICDS_VERSION.zip && \  
unzip symmetric-server-${SYMMETRICDS_VERSION}.zip && \  
cp -r symmetric-server-${SYMMETRICDS_VERSION}/* ${SYMMETRICDS_HOME}/ && \  
rm -rf symmetric-server-${SYMMETRICDS_VERSION}*  
  
#USER symmetricds  
ADD ./data /  
  
RUN chmod 777 /start-symmertic-ds  
  
CMD ["/start-symmertic-ds"]  
  
EXPOSE 31415  
EXPOSE 31416  

