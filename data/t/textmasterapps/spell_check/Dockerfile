FROM debian:stretch  
  
ENV HOME /home/app  
ENV TMP_DIR /tmp/languagetool  
RUN mkdir -p $HOME && mkdir -p $TMP_DIR  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN set -ex \  
&& apt-get update -y \  
&& apt-get install -y --no-install-recommends openjdk-8-jre-headless unzip
curl  
  
ENV VERSION 3.8  
RUN curl --max-time 300
https://www.languagetool.org/download/LanguageTool-$VERSION.zip -o
$TMP_DIR/LanguageTool-$VERSION.zip  
  
RUN set -ex \  
&& unzip $TMP_DIR/LanguageTool-$VERSION.zip -d $TMP_DIR \  
&& mv $TMP_DIR/LanguageTool-$VERSION/* $HOME/ \  
&& rm -rf $TMP_DIR  
  
RUN set -ex \  
&& apt-get clean \  
&& apt-get -y autoremove  
  
WORKDIR $HOME  
  
CMD ["java", "-cp", "languagetool-server.jar",
"org.languagetool.server.HTTPServer", "--port", "80", "--public", "--allow-
origin", "'*'"]  
EXPOSE 80  

