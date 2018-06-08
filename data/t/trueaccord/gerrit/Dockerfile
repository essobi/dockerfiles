FROM ubuntu:14.04  
# accept-java-license  
RUN echo /usr/bin/debconf shared/accepted-oracle-license-v1-1 select true |
/usr/bin/debconf-set-selections  
  
RUN apt-get update && \  
apt-get install -yq git python-software-properties software-properties-common
&& \  
add-apt-repository ppa:webupd8team/java && \  
apt-get remove -yq python-software-properties && \  
apt-get autoremove -yq && \  
apt-get clean -yq && \  
rm -rf /var/lib/apt/lists/*  
  
RUN apt-get update && \  
apt-get install -yq oracle-java8-installer oracle-java8-set-default && \  
apt-get autoremove -yq && \  
apt-get clean -yq && \  
rm -rf /var/lib/apt/lists/*  
  
MAINTAINER jdavis@trueaccord.com  
  
ENV GERRIT_VERSION 2.14  
ENV GERRIT_WAR /gerrit-bin/gerrit.war  
  
RUN mkdir /gerrit-bin && chmod 0755 /gerrit-bin  
  
RUN wget https://www.gerritcodereview.com/download/gerrit-$GERRIT_VERSION.war
-O /gerrit-bin/gerrit.war  
  
ADD init_or_upgrade.sh /  
  
USER root  
RUN adduser --gecos "Gerrit" \--disabled-password --disabled-login gerrit2  
RUN mkdir /gerrit  
RUN chown -R gerrit2:gerrit2 /gerrit  
  
USER gerrit2  
  
EXPOSE 49417 29418  
USER gerrit2  
  
RUN ln -s /gerrit/etc/dot_ssh /home/gerrit2/.ssh  
  
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle  
  
CMD exec bash -c "cd /gerrit; exec ./bin/init.sh run"  
  

