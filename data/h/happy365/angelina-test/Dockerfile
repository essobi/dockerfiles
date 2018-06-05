FROM centos:7.3.1611  
RUN yum install epel-release -y  
RUN yum install wget -y  
ENV URL http://files.happy366.cn/files/docker  
RUN wget -c $URL/rundoc.sh -O /usr/bin/rundoc.sh && \  
wget -c $URL/angelina-test/test.sh -O /usr/bin/test.sh && \  
chmod +x /usr/bin/rundoc.sh && \  
chmod +x /usr/bin/test.sh  

