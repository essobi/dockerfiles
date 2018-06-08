FROM ubuntu:14.04  
MAINTAINER Matt Ho  
  
ENV GO_SERVER 127.0.0.1  
ENV GO_SERVER_PORT 8153  
#--[ DO NOT MODIFY BELOW THIS POINT ]------------------------------------  
ENV GOCD_VERSION 15.2.0  
ENV GOCD_BUILD 2248  
ENV GOCD_DEB go-agent-${GOCD_VERSION}-${GOCD_BUILD}.deb  
  
# install oracle jdk 7  
RUN sed 's/main$/main universe/' -i /etc/apt/sources.list  
RUN apt-get update && apt-get install -y software-properties-common python-
software-properties  
RUN add-apt-repository ppa:webupd8team/java -y  
  
RUN apt-get update  
RUN echo oracle-java7-installer shared/accepted-oracle-license-v1-1 select
true | /usr/bin/debconf-set-selections  
RUN apt-get install -y oracle-java7-installer  
  
ENV JAVA_HOME /usr/lib/jvm/java-7-oracle  
  
# install dependencies  
RUN apt-get update && apt-get install -y curl wget unzip ruby1.9.3  
  
# install go-agent  
ENV AGENT_WORK_DIR /var/lib/go-agent  
ENV DAEMON N  
VOLUME ${AGENT_WORK_DIR}  
RUN curl -L -o /tmp/${GOCD_DEB} http://download.go.cd/gocd-deb/${GOCD_DEB} &&
\  
dpkg -i /tmp/${GOCD_DEB} && \  
rm -f /tmp/${GOCD_DEB}  
  
# rm /etc/default/go-agent; defaults should come from ENV  
RUN rm -f /etc/default/go-agent  
  
#--[ BUILD DEPENDENCIES ]------------------------------------------------  
RUN apt-get update ; \  
apt-get install -y unzip curl wget ruby1.9.3 build-essential ; \  
gem install sass ; \  
gem install fpm ; \  
gem install rake  
  
# install golang  
RUN curl -L -o /tmp/golang.tgz
https://storage.googleapis.com/golang/go1.5.1.linux-amd64.tar.gz ; \  
(cd /usr/local ; tar -xzvf /tmp/golang.tgz) ; \  
rm /tmp/golang.tgz  
  
# install all the vcs tools  
RUN apt-get update && apt-get install -y git subversion bzr mercurial  
  
# connect to various common hosts  
ADD ssh/config /root/.ssh/config  
  
RUN apt-get update && \  
apt-get install -y --force-yes apt-transport-https && \  
apt-get update  
  
# install docker  
RUN apt-key adv --keyserver hkp://pgp.mit.edu:80 --recv-keys
58118E89F3A912897C070ADBF76221572C52609D ; \  
echo "deb https://apt.dockerproject.org/repo ubuntu-trusty main" >
/etc/apt/sources.list.d/docker.list ; \  
apt-get update ; \  
apt-get install -y docker-engine  
  
# install mysql client  
RUN apt-get update && apt-get install -y mysql-client-5.6  
  
# install aws cli  
RUN apt-get update && apt-get install -y awscli  
  
# add java and go to path  
ENV PATH
/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${JAVA_HOME}/bin:/usr/local/go/bin  
  
## add support for slate  
ADD Gemfile /tmp/slate/Gemfile  
RUN cd /tmp/slate && \  
gem install bundler && \  
bundle install  
  
CMD [ "/usr/share/go-agent/agent.sh" ]  
  

