FROM centos:7  
RUN yum -q -y install python-setuptools && \  
yum -q -y install epel-release && \  
yum -q -y install python-apsw && \  
yum clean all  
  
WORKDIR /tmp  
RUN curl -s -O
http://dl.acestream.org/centos/7/acestream_3.0.2_centos_7_amd64.tar.gz && \  
tar -C /usr/local -xvf acestream_3.0.2_centos_7_amd64.tar.gz && \  
rm -rf acestream_3.0.2_centos_7_amd64.tar.gz && \  
mv /usr/local/acestream_3.0.2_centos_7_amd64/usr/local/ssl /usr/local  
COPY acestreamengine.sh /usr/local/bin/acestreamengine  
WORKDIR /  
  
EXPOSE 6878  
EXPOSE 8621  
RUN yum -q -y install expect tcllib telnet && \  
yum clean all  
COPY aceget.exp /usr/local/bin/aceget  
  
ADD https://github.com/krallin/tini/releases/download/v0.10.0/tini
/usr/local/bin/tini  
RUN chmod a+x /usr/local/bin/tini  
  
ADD https://raw.githubusercontent.com/vishnubob/wait-for-it/master/wait-for-
it.sh /usr/local/bin/wait-for-it  
RUN chmod a+x /usr/local/bin/wait-for-it  
  
COPY docker-entrypoint.sh /docker-entrypoint.sh  
ENTRYPOINT ["/usr/local/bin/tini", "-g", "--", "/docker-entrypoint.sh"]  

