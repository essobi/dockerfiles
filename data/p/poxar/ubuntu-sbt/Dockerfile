FROM ubuntu:16.10  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV LAST_UPDATE 2017-06-24  
RUN apt-get -y update \  
&& apt-get -y upgrade \  
&& apt-get -y install ca-certificates wget openjdk-8-jdk scala  
  
ENV SBT_VERSION 0.13.15  
ADD sbt.sha512sum sbt.sha512sum  
RUN wget -nv "https://dl.bintray.com/sbt/debian/sbt-$SBT_VERSION.deb" \  
&& sha512sum -c "sbt.sha512sum" \  
&& dpkg -i "sbt-$SBT_VERSION.deb" \  
&& rm -f "sbt-$SBT_VERSION.deb"  

