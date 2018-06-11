FROM ubuntu:14.04  
RUN apt-get update  
RUN apt-get install -y \  
curl \  
wget  
  
RUN wget -O /tmp/hugo.tar.gz
https://github.com/spf13/hugo/releases/download/v0.12/hugo_0.12_linux_amd64.tar.gz  
RUN tar -xzvf /tmp/hugo.tar.gz -C /opt/  
RUN rm /tmp/hugo.tar.gz  
  
RUN ln -s /opt/hugo_0.12_linux_amd64/hugo_0.12_linux_amd64 /usr/local/bin/hugo  
  
EXPOSE 1313  
COPY blog /var/www  
  
ONBUILD RUN rm -rf /var/www  
  
ENTRYPOINT ["hugo"]  
  
CMD ["serve", "--source=/var/www", "--theme=wolf", "--watch"]

