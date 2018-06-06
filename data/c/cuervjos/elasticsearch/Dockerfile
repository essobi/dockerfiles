FROM ubuntu:12.04  
MAINTAINER cuervjos@gmail.com  
  
  
RUN sed 's/main$/main universe/' -i /etc/apt/sources.list  
RUN apt-get update && apt-mark hold initscripts && apt-get upgrade -y && apt-
get clean # 20140206  
  
# essentials  
RUN apt-get install -y vim curl wget sudo net-tools && \  
apt-get install -y logrotate supervisor openssh-server && \  
apt-get clean  
  
RUN apt-get update && apt-get -y upgrade  
RUN apt-get -y install openjdk-7-jre-headless curl unzip && apt-get clean  
  
ENV JAVA_HOME /usr/lib/jvm/java-7-openjdk-amd64  
  
#ADD authorized_keys /root/.ssh/  
RUN KEYGEN=/usr/bin/ssh-keygen && \  
KEYFILE=/root/.ssh/id_rsa && \  
rm -fr $KEYFILE && \  
$KEYGEN -q -t rsa -N "" -f $KEYFILE && \  
cat $KEYFILE.pub >> /root/.ssh/authorized_keys && \  
echo "== Use this private key to log in ==" && \  
cat $KEYFILE  
RUN chmod 700 /root/.ssh && chmod 600 /root/.ssh/authorized_keys && chown
root:root -R /root/.ssh  
  
ADD resources/ /elasticsearch  
RUN chmod 755 /elasticsearch/es /elasticsearch/setup/install &&
/elasticsearch/setup/install  
  
EXPOSE 22  
EXPOSE 9200  
EXPOSE 9300  
CMD ["start"]  
ENTRYPOINT ["/elasticsearch/es"]  
  

