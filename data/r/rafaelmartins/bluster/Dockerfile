FROM balde/balde:latest  
MAINTAINER Rafael G. Martins <rafael@rafaelmartins.eng.br>  
  
RUN apt-get update && apt-get install -y \  
libcurl4-openssl-dev libjson-glib-dev libmarkdown2-dev spawn-fcgi  
  
RUN git clone https://github.com/rafaelmartins/bluster.git ~/bluster  
  
RUN cd ~/bluster && \  
./autogen.sh && \  
./configure --prefix=/usr && \  
make V=1 && \  
make install  
  
EXPOSE 8080  
CMD ["/usr/bin/spawn-fcgi", "-n", "-a", "0.0.0.0", "-p", "8080", "-u", "www-
data", "--", "/usr/bin/bluster"]  

