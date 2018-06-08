FROM moonshotinternet/ci-scripts:015  
LABEL vendor=Moonshot-Internet  
LABEL com.moonshot.name=ci-frontend  
LABEL com.moonshot.version=1.0.0  
  
ENV HUGO_VERSION 0.35  
ENV HUGO_BINARY hugo_${HUGO_VERSION}_linux-64bit  
  
# Download and Install hugo  
ADD
https://github.com/gohugoio/hugo/releases/download/v${HUGO_VERSION}/${HUGO_BINARY}.tar.gz
/usr/local/  
  
# Extract and Install hugo  
RUN tar xzf /usr/local/${HUGO_BINARY}.tar.gz -C /usr/local/bin/ \  
&& rm /usr/local/${HUGO_BINARY}.tar.gz \  
&& hugo version \  
&& npm install --global gulp-cli gulp  
  
RUN mkdir -p /data  
WORKDIR /data  
VOLUME [ "/data" ]  
CMD ["hugo", "version"]  
EXPOSE 1313  

