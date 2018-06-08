FROM openjdk:jre-slim  
  
LABEL maintainer="Richard Homewood"  
  
RUN apt-get update \  
&& apt-get install ruby-build ruby ruby-dev wget -y  
  
ENV CURL_VERSION 7.30.0  
RUN (wget -O -
http://www.magicermine.com/demos/curl/curl/curl-${CURL_VERSION}.ermine.tar.bz2
| bzip2 -cd \- | tar -xvf -) \  
&& mv /curl-${CURL_VERSION}.ermine/curl.ermine /bin/curl \  
&& rm -rf /curl-${CURL_VERSION}.ermine  
  
## install Riemann and define ENV for overide in docker run  
ENV RIEMANN_VERSION 0.2.14  
RUN curl -skL
https://github.com/riemann/riemann/releases/download/${RIEMANN_VERSION}/riemann-${RIEMANN_VERSION}.tar.bz2
| bzip2 -d | tar -x && \  
mv /riemann-${RIEMANN_VERSION} /app  
  
RUN apt-get remove ruby-build ruby-dev wget -y \  
&& apt autoremove -y \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists  
  
WORKDIR /app  
  
## Change default config to listen on all interfaces  
RUN sed -ie 's/127.0.0.1/0.0.0.0/' etc/riemann.config  
  
EXPOSE 5555/tcp 5555/udp 5556  
CMD [ "bin/riemann", "etc/riemann.config" ]

