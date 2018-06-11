FROM nicholsn/virtuoso  
MAINTAINER Ikuo Matsumura <makiczar@gmail.com>  
  
# Setup AWS CLI  
RUN apt-get update && apt-get -y upgrade  
RUN apt-get -y install curl  
RUN apt-get -y install vim python-pip  
RUN pip install awscli  
RUN mkdir /.aws/  
  
ADD startup.sh /tmp/startup.sh  
RUN chmod a+x /tmp/startup.sh  
ENTRYPOINT ["/tmp/startup.sh"]  
CMD [""]  

