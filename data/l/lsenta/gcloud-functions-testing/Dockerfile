FROM node:6  
MAINTAINER Laurent Senta @lsenta  
  
# Java 8, for Clojurecript.  
# https://linux-tips.com/t/how-to-install-java-8-on-debian-jessie/349/2  
RUN echo "deb http://http.debian.net/debian jessie-backports main" | \  
tee --append /etc/apt/sources.list.d/jessie-backports.list > /dev/null && \  
apt-get -qq update && \  
apt-get install -qy -t jessie-backports openjdk-8-jdk && \  
update-java-alternatives -s java-1.8.0-openjdk-amd64  
  
# Phantomjs  
RUN apt-get -qq update && \  
apt-get install -qy phantomjs  
# Allow phantomjs to run within CLI:  
ENV QT_QPA_PLATFORM offscreen  
  
# Leiningen  
RUN wget
"https://raw.githubusercontent.com/technomancy/leiningen/stable/bin/lein" -O
/usr/bin/lein && \  
chmod +x /usr/bin/lein && \  
lein help  
# Allow lein to run with root user:  
ENV LEIN_ROOT ndb  
  
# Binaries for flow:  
RUN apt-get -qq update && \  
apt-get install -qy ocaml libelf-dev  
  
# Firebase:  
RUN npm install -g firebase-tools@3.9.0  

