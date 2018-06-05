FROM gocd/gocd-agent:16.11.0  
MAINTAINER Altair Six  
  
RUN apt-get update && apt-get install -y wget zip unzip curl telnet phantomjs
python-pip  
RUN pip install awscli  
RUN \  
wget -O /tmp/golang.tar.gz
https://storage.googleapis.com/golang/go1.7.4.linux-amd64.tar.gz && \  
tar -C /usr/local -xzf /tmp/golang.tar.gz && \  
rm /tmp/golang.tar.gz  
  
# add support for docker in docker  
#  
RUN \  
apt-get update && apt-get install -y docker.io && \  
chmod 4755 /usr/bin/docker  
  
# added tool support  
#  
ENV PATH ${PATH}:/usr/local/go/bin:/opt/tools/bin  
RUN echo 'export PATH=${PATH}:/usr/local/go/bin:/opt/tools/bin' >>
/etc/profile  
RUN GOPATH=/opt/tools go get -u github.com/jstemmer/go-junit-report  
  
# added Clojure support  
#  
RUN echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select
true | /usr/bin/debconf-set-selections  
RUN \  
add-apt-repository ppa:webupd8team/java && \  
apt-get update && \  
apt-get install -y oracle-java8-installer  
  
ENV LEIN_ROOT true  
RUN \  
wget -O /bin/lein
https://raw.githubusercontent.com/technomancy/leiningen/stable/bin/lein && \  
chmod +x /bin/lein && \  
su - go -c lein  
  
# added npm support  
#  
RUN curl -sL https://deb.nodesource.com/setup_6.x | sudo -E bash -  
RUN apt-get install -y nodejs  
RUN npm install -g postcss-cli autoprefixer cssnano-cli  
  

