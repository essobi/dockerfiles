FROM ubuntu:xenial  
MAINTAINER Kyle Manna <kyle@kylemanna.com>  
  
ARG USER_ID  
ARG GROUP_ID  
  
ENV HOME /bitcoin  
  
# add user with specified (or default) user/group ids  
ENV USER_ID ${USER_ID:-1000}  
ENV GROUP_ID ${GROUP_ID:-1000}  
RUN groupadd -g ${GROUP_ID} bitcoin  
RUN useradd -u ${USER_ID} -g bitcoin -s /bin/bash -m -d /bitcoin bitcoin  
  
RUN chown bitcoin:bitcoin -R /bitcoin  
  
ADD https://bitcoin.org/bin/bitcoin-core-0.16.0/bitcoin-0.16.0-x86_64-linux-
gnu.tar.gz /tmp/  
RUN tar -xzvf /tmp/bitcoin-0.16.0-x86_64-linux-gnu.tar.gz -C /tmp/ \  
&& cp /tmp/bitcoin-0.16.0/bin/* /usr/local/bin \  
&& cp /tmp/bitcoin-0.16.0/lib/* /usr/local/lib \  
&& rm -rf /tmp/bitcoin-0.16.0-x86_64-linux-gnu.tar.gz  
  
ADD ./bin /usr/local/bin  
RUN chmod a+x /usr/local/bin/*  
  
# For some reason, docker.io (0.9.1~dfsg1-2) pkg in Ubuntu 14.04 has
permission  
# denied issues when executing /bin/bash from trusted builds. Building locally  
# works fine (strange). Using the upstream docker (0.11.1) pkg from  
# http://get.docker.io/ubuntu works fine also and seems simpler.  
USER bitcoin  
  
VOLUME ["/bitcoin"]  
  
EXPOSE 8332 8333 18332 18333  
WORKDIR /bitcoin  
  
CMD ["btc_oneshot"]  

