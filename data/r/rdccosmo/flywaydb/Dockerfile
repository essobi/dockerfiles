FROM centos:7  
MAINTAINER Rodrigo Cosme <rdccosmo@gmail.com>  
RUN yum update -y; \  
yum install -y wget nmap  
RUN useradd -m flyway  
WORKDIR /home/flyway  
RUN mkdir migrations && mkdir bin && \  
wget https://bintray.com/artifact/download/business/maven/flyway-
commandline-3.2.1-linux-x64.tar.gz && \  
tar zxvf flyway-commandline-3.2.1-linux-x64.tar.gz && \  
rm -f flyway-commandline-3.2.1-linux-x64.tar.gz && \  
mv flyway-3.2.1 bin/flyway && \  
chmod a+x bin/flyway  
ENV PATH $PATH:/home/flyway/bin/flyway  
ADD run.sh /home/flyway/run.sh  
RUN chown -R flyway:flyway /home/flyway && chmod +x /home/flyway/run.sh  
USER flyway  
CMD /home/flyway/run.sh  
RUN bash  
  

