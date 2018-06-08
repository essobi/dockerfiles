FROM ubuntu:14.04  
# proper init  
ADD https://github.com/krallin/tini/releases/download/v0.14.0/tini /tini  
RUN chmod +x /tini  
ENTRYPOINT ["/tini", "--"]  
  
# install Java  
RUN echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select
true | debconf-set-selections && \  
apt-get update && \  
apt-get install -y software-properties-common && \  
add-apt-repository -y ppa:webupd8team/java && \  
apt-get update && \  
apt-get install -y oracle-java8-installer && \  
rm -rf /var/lib/apt/lists/* && \  
rm -rf /var/cache/oracle-jdk8-installer  
  
# define commonly used JAVA_HOME variable  
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle  
  
# install mark2 and run.sh dependencies  
RUN apt-get update && \  
apt-get -y install \  
git gawk libssl-dev python-dev python-feedparser \  
python-psutil python-twisted-core python-twisted-mail \  
python-twisted-web python-twisted-words python-urwid && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN locale-gen "en_US.UTF-8" && \  
dpkg-reconfigure locales  
  
# Install mark2  
RUN git clone https://github.com/gsand/mark2.git && \  
(cd mark2 && git checkout 95fca2c37a26bf7e43afb37125c22c91e89111d8) && \  
ln -s $PWD/mark2/mark2 /usr/bin/mark2  
  
VOLUME /minecraft/volumes  
EXPOSE 25565  
WORKDIR /minecraft  
ADD run.sh /minecraft/run.sh  
  
CMD ["bash", "run.sh"]  

