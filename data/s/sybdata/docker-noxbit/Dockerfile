FROM lsiobase/alpine:3.7  
# install packages and symlink libs  
RUN \  
apk add --no-cache \  
curl \  
tar \  
nano \  
mc && \  
mkdir -p \  
/opt/noxbit && \  
# install noxbit  
curl -o \  
/tmp/noxbit.tar.gz -L \  
"http://download.noxbit.com/noxbit-pa-x86-64.tar.gz" && \  
tar xf \  
/tmp/noxbit.tar.gz \  
-C /opt/noxbit && \  
# cleanup  
rm -rf \  
/tmp/*  
  
# add local files  
COPY root/ /  
  
# ports and volumes  
EXPOSE 6689 6881 6882 6883 6884 6885 6886 6887 6888 6889 6890 6891 6892 6893
6894 6895 6896 6897 6898 6899 6900  
VOLUME /config  
VOLUME /var/log  

