FROM alpine:latest  
  
#install languagetool  
WORKDIR /tmp  
ADD https://languagetool.org/download/LanguageTool-3.4.zip
/tmp/LanguageTool-3.4.zip  
RUN /bin/true \  
&& apk update \  
&& apk update && apk upgrade \  
&& apk add zip \  
openjdk8-jre-base \  
&& unzip /tmp/LanguageTool-3.4.zip \  
&& mv /tmp/LanguageTool-3.4 /usr/languagetool \  
&& rm /tmp/* \  
&& apk del zip \  
&& rm -rf /var/cache/apk/*  

