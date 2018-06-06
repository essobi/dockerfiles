###  
#  
# Bisq Dockerfile installation:  
#  
# build:  
#  
# docker build -t bisq-0.5.2 .  
#  
# run:  
# You can run it from an X11 capable linux client like this:  
# xhost +  
# docker run -v /tmp/.X11-unix:/tmp/.X11-unix -e DISPLAY=unix$DISPLAY
bisq-0.5.2  
#  
###  
FROM maven:3.5-jdk-8  
# maintainer details  
MAINTAINER Cédric Walter "cedric.walter@gmail.com"  
# add openjfx  
RUN apt-get update \  
&& apt-get install --no-install-recommends -y \  
openjfx \  
unzip \  
&& apt-get clean \  
&& rm -f /var/lib/apt/lists/*_dists_*  
  
# save repository  
COPY settings-docker.xml /usr/share/maven/ref/  
  
# clone and install bitcoinj_version  
WORKDIR /local/git  
RUN git clone -b bisq_0.14.4.1 https://github.com/bitsquare/bitcoinj.git  
WORKDIR /local/git/bitcoinj  
RUN mvn clean install -DskipTests -gs /usr/share/maven/ref/settings-docker.xml  
  
WORKDIR /local/git  
RUN git clone https://github.com/bitsquare/libdohj.git  
WORKDIR /local/git/libdohj  
RUN mvn clean install -DskipTests -gs /usr/share/maven/ref/settings-docker.xml  
  
WORKDIR /local/git  
RUN git clone https://github.com/bitsquare/btcd-cli4j.git  
WORKDIR /local/git/btcd-cli4j  
RUN mvn clean install -DskipTests -gs /usr/share/maven/ref/settings-docker.xml  
  
WORKDIR /local/git  
RUN git clone https://github.com/bitsquare/bitsquare.git  
WORKDIR /local/git/bitsquare  
RUN mvn clean install -DskipTests -gs /usr/share/maven/ref/settings-docker.xml  
WORKDIR /local/git/  
  
VOLUME /home/root/.local/share/Bitsquare  
CMD java -jar /local/git/bitsquare/gui/target/shaded.jar  

