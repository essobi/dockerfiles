FROM debian:jessie  
  
RUN apt-get update && apt-get -y install \  
git-core \  
make \  
gcc  
  
RUN git clone https://github.com/solusipse/fiche.git \  
&& cd /fiche \  
&& make  
  
RUN mkdir /app && mv /fiche/fiche /app/ \  
&& rm -vrf /fiche  
  
EXPOSE 9999  
ENTRYPOINT ["/app/fiche"]  

