FROM ubuntu:xenial  
MAINTAINER Yves Dubromelle <yves+git@dubronetwork.fr>  
  
# Packages installation  
RUN apt-get update && \  
apt-get install -y taskd  
  
# Taskd configuration  
ENV TASKDDATA /var/lib/taskd  
ENV TASKDCONF /etc/taskd  
ENV TASKDPKI /usr/share/taskd/pki  
RUN taskd init  
COPY taskd-config ${TASKDCONF}/config  
  
# Cerfiticates initialisation  
WORKDIR ${TASKDPKI}  
RUN ./generate && \  
cp *.pem ${TASKDDATA} && \  
taskd add org Default  
  
VOLUME ${TASKDDATA}  
EXPOSE 53589  
  
CMD ["taskd", "server"]  

