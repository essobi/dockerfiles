FROM java:8-jdk  
  
VOLUME /data/services  
  
EXPOSE 80 443 8080 8443  
ADD ./restart.sh /restart.sh  
ADD ./run.sh /run.sh  
  
# install watchman  
WORKDIR /  
RUN apt-get -qq update  
RUN apt-get install -y inotify-tools automake build-essential python-
setuptools  
RUN git clone https://github.com/facebook/watchman.git &&\  
cd watchman &&\  
git checkout v3.5.0 &&\  
./autogen.sh &&\  
./configure &&\  
make &&\  
make install  
  
RUN echo '["watch", "/data/services"]' |\  
watchman -j  
  
RUN echo '[ "trigger", "/data/services", { "name": "app", "match": "*.jar",
"command": ["/bin/bash", "/restart.sh"], "stdout": ">>/tmp/app.log" } ]' |\  
watchman -j  
  
CMD ["sh","run.sh"]

