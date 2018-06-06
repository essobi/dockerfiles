# word2vec for Debian jessie  
#  
# URL: https://github.com/William-Yeh/docker-word2vec  
#  
# Reference: https://code.google.com/p/word2vec/  
# See also: https://github.com/William-Yeh/word2vec-mac  
#  
# Version 0.1  
#  
# pull base image  
FROM debian:jessie  
MAINTAINER William Yeh <william.pjyeh@gmail.com>  
  
  
RUN mkdir -p /opt/word2vec /opt/word2vec/demo  
WORKDIR /opt/word2vec  
  
RUN DEBIAN_FRONTEND=noninteractive apt-get update && \  
apt-get install -y subversion make gcc curl && \  
\  
\  
\  
svn checkout http://word2vec.googlecode.com/svn/trunk/ && \  
cd trunk && \  
sed -i -e \  
's/TrainModel();/if (vocab_hash == 0) { printf("ERROR: no enough memory;
should be >= %zu bytes.", vocab_hash_size * sizeof(int)); } else {
TrainModel(); } \/\/ avoid "segmentation fault" error/' \  
word2phrase.c && \  
make && \  
\  
\  
\  
cd /opt/word2vec && \  
mv trunk/compute-accuracy . && \  
mv trunk/distance . && \  
mv trunk/word-analogy . && \  
mv trunk/word2phrase . && \  
mv trunk/word2vec . && \  
mv trunk/questions-*.txt demo && \  
\  
\  
\  
cd /opt/word2vec/demo && \  
curl -O http://mattmahoney.net/dc/text8.zip && \  
\  
\  
\  
rm -rf /opt/word2vec/trunk && \  
apt-get remove -y --auto-remove subversion make gcc curl && \  
apt-get clean  
  
#----------------------------#  
# configure  
VOLUME [ "/data" ]  
WORKDIR /data  
  
# for convenience  
ENV WORD2VEC_PATH /opt/word2vec  
ENV PATH /opt/word2vec:/opt/word2vec/demo:$PATH  
COPY usage.sh /opt/word2vec/  
COPY demo /opt/word2vec/demo  
RUN date '+%Y-%m-%dT%H:%M:%S%:z' > /var/log/DOCKER_BUILD_TIME  
  
# Define default command.  
CMD ["usage.sh"]  

