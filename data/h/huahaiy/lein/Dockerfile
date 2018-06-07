#  
# Use lein to run Clojure application as a user "app"  
#  
# Version 0.6  
#  
  
FROM huahaiy/oracle-java  
  
MAINTAINER Huahai Yang <hyang@juji.io>  
  
ENV LEIN_ROOT true  
  
RUN \  
apt-get update && \  
apt-get -y upgrade && \  
echo "===> download leiningen..." && \  
wget -q -O /usr/bin/lein \  
https://raw.githubusercontent.com/technomancy/leiningen/stable/bin/lein && \  
chmod +x /usr/bin/lein  
  
#RUN \  
#echo "===> create app user" && \  
#mkdir -p /home/app && \  
#groupadd -r app && \  
#useradd -r -g app -d /home/app -s /sbin/nologin -c "Lein user" app && \  
#chown -R app:app /home/app  
  
#USER app  
  
#ENTRYPOINT ["lein"]  

