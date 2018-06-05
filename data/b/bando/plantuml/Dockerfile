FROM java:alpine  
MAINTAINER bando-shintaro <bando142141@gmail.com>  
  
RUN apk --no-cache add ca-certificates graphviz jpeg-dev zlib-dev ttf-dejavu
freetype-dev openssl \  
&& apk --no-cache --virtual=dependencies add wget \  
&& update-ca-certificates \  
&& apk del dependencies  
  
RUN wget http://ipafont.ipa.go.jp/old/ipafont/ipag00303.php \  
&& unzip ipag00303.php \  
&& mkdir -p /usr/share/fonts/ipa \  
&& mv ipag00303/ipag.ttf /usr/share/fonts/ipa/ \  
&& fc-cache -fv \  
&& rm -rf ipag00303 ipag00303.php  
  
#PlantUML  
ENV PLANTUML_DIR /plantuml  
  
RUN mkdir $PLANTUML_DIR  
WORKDIR $PLANTUML_DIR  
  
RUN wget http://sourceforge.net/projects/plantuml/files/plantuml.jar/download
-O $PLANTUML_DIR/plantuml.jar  
  
ENTRYPOINT ["java","-jar","plantuml.jar"]  

