FROM cuongdd1/cloud-provisioning-packs  
MAINTAINER anhln4@fsoft.com.vn  
RUN apt-get update && apt-get install -y git  
  
RUN mkdir /installation  
WORKDIR /installation  
COPY . /installation  
VOLUME /root/.aws/  
  
RUN wget --no-check-certificate --no-cookies --header "Cookie:
oraclelicense=accept-securebackup-cookie" http://download.oracle.com/otn-
pub/java/jdk/8u77-b03/jdk-8u77-linux-x64.tar.gz  
RUN tar xzvf jdk-8u77-linux-x64.tar.gz  
RUN sed -i '$ a\export JAVA_HOME=/installation/jdk1.8.0_77' ~/.bashrc  
RUN sed -i '$ a\export PATH=\$JAVA_HOME/bin:$PATH' ~/.bashrc  
  
RUN wget
http://mirror.downloadvn.com/apache/maven/maven-3/3.3.9/binaries/apache-
maven-3.3.9-bin.tar.gz  
RUN tar xzvf apache-maven-3.3.9-bin.tar.gz  
RUN sed -i '$ a\export MVN_HOME=/installation/apache-maven-3.3.9' ~/.bashrc  
RUN sed -i '$ a\export PATH=\$MVN_HOME/bin:$PATH' ~/.bashrc  
  
RUN mkdir -p /root/.ssh/  
ADD ssh/id_rsa /root/.ssh/id_rsa  
RUN chmod 600 /root/.ssh/id_rsa  
RUN touch /root/.ssh/known_hosts && ssh-keyscan bitbucket.org >>
/root/.ssh/known_hosts  
ADD flows/settings.js /root/.node-red/settings.js  
ADD flows/flows.json /root/.node-red/flows.json  
  
RUN ./app-deploy "R1" "YES" "citus-apps-management" "/root"  
  
EXPOSE 1880  
ENTRYPOINT ["pm2"]  
CMD ["start", "node-red", "--no-daemon"]  

