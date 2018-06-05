FROM httpd:2  
RUN apt-get update && apt-get install -y curl  
  
# Install hugo  
RUN curl -L -o /tmp/hugo.tar.gz
https://github.com/gohugoio/hugo/releases/download/v0.19/hugo_0.19_Linux-32bit.tar.gz  
RUN tar xvf /tmp/hugo.tar.gz -C /tmp/  
RUN mv /tmp/hugo_0.19_linux_386/hugo_0.19_linux_386 /usr/bin/hugo  
  
# copy config  
COPY ./conf/ /usr/local/apache2/conf/  
  
# copy source and generate result  
COPY ./hugo/ /src/  
RUN hugo -s /src/ --baseUrl="http://www.gordonburgett.net"  
RUN rm -r /usr/local/apache2/htdocs && mv /src/public
/usr/local/apache2/htdocs  

