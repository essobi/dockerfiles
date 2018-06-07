FROM inklabs/php-fpm:5.6  
LABEL maintainer="Jamie Isaacs <pdt256@gmail.com>"  
  
USER root  
  
RUN apt-get update \  
&& apt-get -y install \  
supervisor \  
default-jre \  
imagemagick \  
&& ( \  
cd /usr/local/src \  
&& curl -fsSL
http://apache.cs.utah.edu/xmlgraphics/fop/binaries/fop-1.1-bin.tar.gz -o
fop-1.1-bin.tar.gz \  
&& tar zxf fop-1.1-bin.tar.gz \  
) \  
&& ln -s /usr/local/src/fop-1.1/fop /usr/local/bin/  
  
ENV JAVA_HOME /usr/lib/jvm/java-7-openjdk-amd64  
  
CMD ["supervisord", "-n"]  

