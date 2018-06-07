FROM debian  
  
MAINTAINER Manuel Mueller  
  
RUN apt-get update  
  
RUN apt-get install -y gnupg  
RUN echo "deb http://dl.bintray.com/deepstreamio/deb jessie main" | tee -a
/etc/apt/sources.list  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys
379CE192D401AB61  
RUN apt-get update  
RUN apt-get install -y deepstream.io  
  
# add config files  
ADD ./conf /etc/deepstream  
  
# Installing Plugins  
RUN deepstream install storage postgres && \  
deepstream install storage elasticsearch && \  
deepstream install storage mongodb && \  
deepstream install storage rethinkdb && \  
deepstream install cache redis && \  
deepstream install cache hazelcast && \  
deepstream install cache memcached  
  
# ws port  
EXPOSE 6020  
# http port  
EXPOSE 8080  
# Define default command.  
CMD [ "deepstream" ]  

