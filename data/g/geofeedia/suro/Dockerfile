FROM netflixoss/java:7  
RUN apt-get update &&\  
apt-get -y install git &&\  
git clone https://github.com/Netflix/suro.git /usr/local/src/suro &&\  
cd /usr/local/src/suro &&\  
git checkout v0.2.10-rc.4 &&\  
./gradlew installApp &&\  
mv /usr/local/src/suro/suro-server/build/install/suro-server /opt/suro &&\  
rm -rf /usr/local/src/suro  
  
EXPOSE 7101 7103  
WORKDIR /opt/suro  
  
VOLUME /opt/suro/conf  
  
ENTRYPOINT ["./bin/suro-server"]  
CMD ["-m", "conf/routingmap.json", "-s", "conf/sink.json", "-i",
"conf/input.json"]  

