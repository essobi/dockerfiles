FROM ringo/scientific:6.5  
RUN yum install -y wget unzip  
RUN mkdir -p /home/src/ && cd /home/src && wget --no-check-certificate --no-
cookies --header "Cookie: oraclelicense=accept-securebackup-cookie"
http://download.oracle.com/otn-pub/java/jdk/8u5-b13/jdk-8u5-linux-x64.rpm &&
rpm -ivh jdk-8u5-linux-x64.rpm  
RUN cd /home/src && wget http://downloads.typesafe.com/typesafe-
activator/1.2.2/typesafe-activator-1.2.2.zip && unzip typesafe-
activator-1.2.2.zip  
RUN ln -s /home/src/activator-1.2.2 /usr/local/lib/activator && ln -s
/usr/local/lib/activator/activator /usr/local/bin/activator  
  

