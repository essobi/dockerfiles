FROM ubuntu:16.04  
RUN apt-get update && \  
apt-get install -y curl apt-transport-https supervisor  
  
RUN curl 'https://bintray.com/user/downloadSubjectPublicKey?username=pcp' |
apt-key add -  
  
RUN echo "deb https://dl.bintray.com/pcp/xenial xenial main" | tee -a
/etc/apt/sources.list  
  
RUN apt-get update && \  
apt-get install -y pcp pcp-webapi  
  
COPY supervisor.conf /etc/supervisor/supervisord.conf  
COPY pmwebd.options /etc/pcp/pmwebd/pmwebd.options  
  
EXPOSE 9990  
CMD /usr/bin/supervisord -c /etc/supervisor/supervisord.conf  

