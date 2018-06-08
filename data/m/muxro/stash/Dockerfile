FROM ubuntu:trusty  
  
# add ``Oracle Java JRE`` to repository (what's weird is that this key
presents as ``Launchpad VLC``)  
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys EEA14886 \  
&& echo "deb http://ppa.launchpad.net/webupd8team/java/ubuntu $(lsb_release
-cs) main" \  
> /etc/apt/sources.list.d/launchpad-webupd8team-java.list \  
&& echo debconf shared/accepted-oracle-license-v1-1 select true \  
| sudo debconf-set-selections \  
&& echo debconf shared/accepted-oracle-license-v1-1 seen true \  
| sudo debconf-set-selections  
  
# install ``cURL`` and ``Java 7 JRE`` which is supported by ``Atlassian
stash``  
RUN apt-get update -qq \  
&& apt-get install -qqy wget curl oracle-java7-installer git  
  
# setup primary environment variables  
ENV JAVA_HOME /usr/lib/jvm/java-7-oracle  
ENV STASH_HOME /home/stash  
# setup secondary environment helper variables  
ENV STASH_VERSION 3.1.3  
# create non-root user to run ``Atlassian stash``  
RUN useradd --create-home --comment "Account for running Stash" stash \  
&& chmod -R a+rw ~stash  
  
# download ``Atlassian stash`` standalone archive version  
RUN wget "http://www.atlassian.com/software/stash/downloads/binary/atlassian-
stash-${STASH_VERSION}.tar.gz" \  
&& tar -xzf "atlassian-stash-${STASH_VERSION}.tar.gz" \  
&& rm "atlassian-stash-${STASH_VERSION}.tar.gz" \  
&& mkdir -p /usr/local/atlassian \  
&& mv "atlassian-stash-${STASH_VERSION}" /usr/local/atlassian/stash \  
&& chown -R stash:stash /usr/local/atlassian/stash \  
&& chmod -R 777 /usr/local/atlassian/stash/temp \  
&& chmod -R 777 /usr/local/atlassian/stash/logs \  
&& chmod -R 777 /usr/local/atlassian/stash/work  
  
# set the principal user as new non-root stash account  
USER stash  
  
# expose default HTTP and tomcat shutdown port  
EXPOSE 7999  
# set volume mount points for ``Atlassian stash`` installation and home
directory  
VOLUME ["/home/stash", "/usr/local/atlassian/stash"]  
  
# run ``Atlassian stash`` as a foreground process  
CMD /usr/local/atlassian/stash/bin/start-stash.sh -fg  

