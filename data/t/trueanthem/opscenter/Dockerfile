FROM debian  
  
RUN apt-get update && apt-get install -y curl  
  
RUN echo "deb http://debian.datastax.com/community stable main" | tee -a
/etc/apt/sources.list.d/datastax.community.list  
RUN curl -L https://debian.datastax.com/debian/repo_key | apt-key add -  
  
RUN apt-get update  
RUN apt-get install -y openjdk-7-jre  
  
RUN apt-get install -y opscenter  
  
EXPOSE 8888  
#ENTRYPOINT /usr/share/opscenter/bin/opscenter -f  

