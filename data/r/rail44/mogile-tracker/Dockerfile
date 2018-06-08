FROM ubuntu:trusty  
RUN apt-get update  
RUN apt-get upgrade -y  
  
RUN apt-get install -y cpanminus build-essential libmysqlclient-dev  
  
RUN cpanm install --force MogileFS::Server  
RUN cpanm install DBD::mysql  
RUN cpanm install MogileFS::Utils  
  
RUN mkdir /tracker  
WORKDIR /tracker  
ADD ./mogilefsd.conf /tracker/mogilefsd.conf  
ADD ./run.sh /tracker/run.sh  
EXPOSE 7001  
CMD ["./run.sh"]  

