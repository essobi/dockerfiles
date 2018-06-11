FROM panos/spark  
  
LABEL maintainer "Panayiotis Vlantis <vlantis.p@gmail.com>"  
  
LABEL name "Apache Zeppelin"  
  
LABEL version "0.9-2eb084a221377"  
  
# Install Zeppelin  
#  
RUN true \  
&& set -o pipefail \  
&& mkdir /opt/zeppelin \  
&& curl -s ftp://vlantis.gr/pub/zeppelin-0.9.0-SNAPSHOT.tar.gz \  
| gunzip \  
| tar x --strip=1 -C /opt/zeppelin  
  
ENV ZEPPELIN_HOME /opt/zeppelin  
  
ENV PATH $ZEPPELIN_HOME/bin:$PATH  
  
ENV ZEPPELIN_PORT 8888  
EXPOSE 8888  
## Add user and change /opt/livy owner to user  
#  
RUN true \  
&& useradd --uid 1000 --comment user user \  
&& chown -R 1000:1000 $ZEPPELIN_HOME  
  
## Run the rest commands as user  
#  
USER user  
ENV USER user  
ENV HOME /home/user  
WORKDIR $HOME  
  
CMD "zeppelin.sh"  

