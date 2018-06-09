FROM java:8  
MAINTAINER Marcin Lagowski <marcinlagowski92@gmail.com>  
  
RUN mkdir /app  
WORKDIR /app  
  
COPY target/universal/testifyapi-1.0-SNAPSHOT.zip /app  
  
CMD /app/testifyapi-1.0-SNAPSHOT/bin/testifyapi  
  
#RUN apt-get update && apt-get install -y --no-install-recommends ca-
certificates curl wget && rm -rf /var/lib/apt/lists/*  
#  
#RUN mkdir /app  
#RUN mkdir /app-tmp  
#WORKDIR /app-tmp  
#ADD . /app-tmp  
#  
#RUN curl -O https://downloads.typesafe.com/play/2.2.6/play-2.2.6.zip && \  
# unzip play-2.2.6.zip -d / && \  
# rm play-2.2.6.zip && \  
# chmod a+x /play-2.2.6/play && \  
# /play-2.2.6/play dist && \  
# unzip /app-tmp/target/universal/testifyapi-1.0-SNAPSHOT.zip -d /app && \  
# rm -rf /play-2.2.6 && \  
# rm -rf /app-tmp && \  
# rm -rf ~/.m2 && \  
# rm -rf ~/.ivy2  
#  
#  
#WORKDIR /app  
#  
#CMD /app/testifyapi-1.0-SNAPSHOT/bin/testifyapi

