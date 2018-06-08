FROM ubuntu:xenial  
  
LABEL ravendb-version="40016-beta"  
LABEL operating-system="ubuntu"  
  
ENV RAVEN_Port 8080  
ENV RAVEN_Url "http://0.0.0.0:8080"  
ENV RAVEN_Hostname localhost  
ENV RAVEN_TCP_Port 38888  
ENV RAVEN_TCP_Url "tcp://0.0.0.0:38888"  
ENV RAVEN_DataDir /var/lib/ravendb/  
ENV RAVEN_AllowAnonymous true  
ENV RAVEN_LogsMode Information  
  
# Update container  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
&& apt-get install bzip2 libunwind8 libicu55 libcurl3 ca-certificates -y  
  
# RavenDB  
EXPOSE ${RAVEN_Port} ${RAVEN_TCP_Port}  
VOLUME ${RAVEN_DataDir}  
  
# Extract RavenDB files  
ADD
http://hibernatingrhinos.com/downloads/RavenDB%20for%20Ubuntu%2016.04%20x64/40016-Beta
/home/Raven.tar.bz2  
RUN cd /home \  
&& mkdir Raven \  
&& tar xf Raven.tar.bz2 -C Raven \  
&& rm /home/Raven.tar.bz2 \  
&& apt-get remove bzip2 -y \  
&& apt-get autoremove -y \  
&& rm -rf /var/lib/apt/lists/*  
  
# Run  
WORKDIR /home/Raven/Server  
CMD ./Raven.Server \  
/Raven/ServerUrl=${RAVEN_Url} \  
/Raven/ServerUrl/Tcp=${RAVEN_TCP_Url} \  
/Raven/HostName=${RAVEN_Hostname} \  
/Raven/AllowAnonymousUserToAccessTheServer=${RAVEN_AllowAnonymous} \  
/Raven/DataDir=${RAVEN_DataDir} \  
/Raven/Logs.Mode=${RAVEN_LogsMode} \  
\--daemon \  
\--print-id

