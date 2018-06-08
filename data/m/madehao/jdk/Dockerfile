FROM madehao/centos:7  
MAINTAINER madehao1983@sina.com  
  
WORKDIR /tmp  
  
RUN curl -L \  
"http://download.oracle.com/otn-
pub/java/jdk/8u171-b11/512cd62ec5174c3487ac17c61aaa89e8/jdk-8u171-linux-x64.rpm"
\  
-H "Cookie: oraclelicense=accept-securebackup-cookie" \  
-H "Connection: keep-alive" -O \  
# install jdk  
&& rpm -ivh jdk-8u171-linux-x64.rpm \  
# remove downloaded file  
&& rm -f jdk-8u171-linux-x64.rpm  
  
WORKDIR /  

