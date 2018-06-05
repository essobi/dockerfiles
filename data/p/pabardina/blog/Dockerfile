FROM debian:wheezy  
MAINTAINER pa@bardina.net  
  
ENV HUGO_VERSION 0.15  
ENV HUGO_BINARY hugo_${HUGO_VERSION}_linux_amd64  
  
ADD
https://github.com/spf13/hugo/releases/download/v${HUGO_VERSION}/${HUGO_BINARY}.tar.gz
/usr/local/  
RUN tar xzf /usr/local/${HUGO_BINARY}.tar.gz -C /usr/local/ \  
&& ln -s /usr/local/${HUGO_BINARY}/${HUGO_BINARY} /usr/local/bin/hugo \  
&& rm /usr/local/${HUGO_BINARY}.tar.gz  
  
ADD site/ /usr/share/blog  
WORKDIR /usr/share/blog  
  
EXPOSE 1313  
CMD hugo server --watch --baseUrl=${HUGO_BASE_URL} \--port=1313
--appendPort=False --bind=0.0.0.0  

