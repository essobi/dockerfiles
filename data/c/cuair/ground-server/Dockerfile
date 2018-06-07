FROM ubuntu:14.04  
WORKDIR /ground-server  
EXPOSE 9000  
# Install prerequisites  
RUN sudo apt-get update && \  
sudo apt-get -y upgrade && \  
sudo apt-get -qq install -y software-properties-common && \  
sudo add-apt-repository ppa:webupd8team/java && \  
sudo apt-get update && \  
sudo apt-get -qq install -y \  
build-essential \  
curl \  
htop \  
tcl8.5  
  
# Install Java 8  
RUN (echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select
true | /usr/bin/debconf-set-selections) && \  
sudo apt-get -qq install -y \  
oracle-java8-installer \  
oracle-java8-set-default  
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle  
ENV PATH $JAVA_HOME/bin:$PATH  
  
# Install git and other dependencies  
RUN sudo apt-get -qq install -y \  
git \  
nodejs \  
npm \  
postgresql \  
postgresql-client-common \  
postgresql-common \  
postgresql-contrib \  
scala \  
unzip  
  
# Setup NodeJS  
RUN ln -s /usr/bin/nodejs /usr/bin/node  
ENV NODE_PATH /usr/local/lib/node_modules  
  
# Setup PostgreSQL  
ENV PGHOST localhost  
COPY docker/db-start.sh docker/db-start.sh  
COPY docker/db-setup.sh docker/db-setup.sh  
RUN docker/db-start.sh && docker/db-setup.sh  
  
# Install SBT  
RUN wget http://dl.bintray.com/sbt/debian/sbt-0.13.8.deb && \  
sudo dpkg -i sbt-0.13.8.deb && \  
sudo apt-get update && \  
sudo apt-get -qq install -y sbt && \  
rm sbt-0.13.8.deb  
  
# Install Activator  
RUN wget http://downloads.typesafe.com/typesafe-activator/1.3.2/typesafe-
activator-1.3.2.zip && \  
unzip typesafe-activator-1.3.2.zip && \  
rm typesafe-activator-1.3.2.zip && \  
mv activator-1.3.2/activator . && \  
mv activator-1.3.2/activator-launch-1.3.2.jar .  
  
COPY app app  
COPY conf conf  
COPY project project  
COPY build.sbt build.sbt  
  
# Launch activator compile task to resolve remaining dependencies  
RUN sbt run && kill $(pgrep -f '.*sbt.*')  
  
COPY public public  
  
CMD docker/db-start.sh && sbt run  

