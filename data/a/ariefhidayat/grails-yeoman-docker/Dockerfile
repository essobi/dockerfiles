FROM onesysadmin/grails:2.3  
MAINTAINER Arief Hidayat <mr.arief.hidayat@gmail.com>  
  
RUN java -version  
RUN gvm-wrapper.sh default grails 2.3.11  
ENV GRAILS_HOME /.gvm/grails/current  
ENV PATH $GRAILS_HOME/bin:$PATH  
  
RUN apt-get -y update  
  
# install python-software-properties (so you can do add-apt-repository)  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y -q python-software-
properties software-properties-common  
  
# install SSH server so we can connect multiple times to the container  
RUN apt-get -y install openssh-server && mkdir /var/run/sshd  
  
# install utilities  
RUN apt-get -y install vim git sudo zip bzip2 fontconfig curl  
  
# install maven  
RUN apt-get -y install maven  
  
# install node.js from PPA  
RUN add-apt-repository ppa:chris-lea/node.js  
RUN apt-get update  
RUN apt-get -y install nodejs  
  
# install yeoman  
RUN npm install -g yo bower  
  
# configure the "hida" and "root" users  
RUN echo 'root:hida' |chpasswd  
RUN groupadd hida && useradd hida -s /bin/bash -m -g hida -G hida && adduser
hida sudo  
RUN echo 'hida:hida' |chpasswd  
  
# expose the working directory, the Tomcat port, the Grunt server port, the
SSHD port, and run SSHD  
VOLUME ["/hida"]  
EXPOSE 8080  
EXPOSE 9000  
EXPOSE 22  
CMD ["grails"]  
  
# install the sample app to download all Maven dependencies  
RUN cd /home/hida && \  
git clone https://github.com/arief-hidayat/grails-practice.git  
RUN cd /home && chown -R hida:hida /home/hida  
RUN cd /home/hida/grails-practice && gvm-exec.sh grails clean && gvm-exec.sh
grails compile  
  
CMD /usr/sbin/sshd -D  

