FROM galloplabs/oracle-jdk  
MAINTAINER Jonathon W. Marshall "jonathon@gallop.io"  
RUN wget -q http://yum.postgresql.org/9.3/redhat/rhel-6-x86_64/pgdg-
centos93-9.3-1.noarch.rpm  
RUN rpm -ivh pgdg-centos93-9.3-1.noarch.rpm \  
&& rm pgdg-centos93-9.3-1.noarch.rpm  
  
RUN yum update -y  
RUN yum install -y tar postgresql93  
  
RUN wget -q https://dl.bintray.com/sbt/native-
packages/sbt/0.13.8/sbt-0.13.8.tgz \  
&& tar -xf sbt-0.13.8.tgz && rm sbt-0.13.8.tgz \  
&& mv sbt /usr/local  
  
ENV PATH $PATH:/usr/local/sbt/bin  

