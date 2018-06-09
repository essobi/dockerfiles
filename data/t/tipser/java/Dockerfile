FROM centos:centos7  
  
# download and install java  
WORKDIR /tmp  
RUN yum install -y curl  
RUN curl -O -L --header "Cookie: oraclelicense=accept-securebackup-cookie;
s_nr=1404891902010; s_cc=true;
gpw_e24=http%3A%2F%2Fwww.oracle.com%2Ftechnetwork%2Fjava%2Fjavase%2Fdownloads%2Fjre7-downloads-1880261.html;
s_sq=oracleotnlive%2Coracleglobal%3D%2526pid%253Dotn%25253Aen-
us%25253A%25252Fjava%25252Fjavase%25252Fdownloads%25252Fjre7-downloads-1880261.html%2526pidt%253D1%2526oid%253Dfunctiononclick(event)%25257BacceptAgreement(window.self%25252C'jre-7u65-oth-
JPR')%25253B%25257D%2526oidt%253D2%2526ot%253DRADIO; gpv_p24=no%20value"
http://download.oracle.com/otn-pub/java/jdk/7u65-b17/jre-7u65-linux-x64.rpm  
RUN rpm -i jre-7u65-linux-x64.rpm  
RUN rm -f jre-7u65-linux-x64.rpm  
  
# add java user for running app  
RUN useradd -ms /bin/bash java  

