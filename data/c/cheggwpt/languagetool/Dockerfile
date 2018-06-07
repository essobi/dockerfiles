FROM cheggwpt/java:0.0.5  
# add wget  
RUN apk --update --no-cache add \  
\--virtual .base_package wget && \  
rm -rf /var/cache/apk/*  
  
# LANGUAGE TOOLS  
ENV LANGUAGETOOL_VERSION 3.4  
RUN wget -q
https://languagetool.org/download/LanguageTool-$LANGUAGETOOL_VERSION.zip -P
/tmp && \  
unzip /tmp/LanguageTool-$LANGUAGETOOL_VERSION.zip -d /usr/local && \  
ln -s /usr/local/LanguageTool-$LANGUAGETOOL_VERSION /usr/local/languagetool &&
\  
rm /tmp/LanguageTool-$LANGUAGETOOL_VERSION.zip  
  
ENV LINK_PATH /v2/check  
  
# Add the files  
COPY container_confs /  
  
EXPOSE 8081  

