FROM phusion/baseimage  
MAINTAINER Holger Schinzel <holger@polis.org>  
  
ARG USER_ID  
ARG GROUP_ID  
  
ENV HOME /polis  
  
# add user with specified (or default) user/group ids  
ENV USER_ID ${USER_ID:-1000}  
ENV GROUP_ID ${GROUP_ID:-1000}  
RUN groupadd -g ${GROUP_ID} polis  
RUN useradd -u ${USER_ID} -g polis -s /bin/bash -m -d /polis polis  
  
RUN chown polis:polis -R /polis  
  
ADD
https://github.com/polispay/polis/releases/download/v1.2.2/poliscore-1.2.2-linux64.tar.gz
/tmp/  
RUN tar -xvf /tmp/poliscore-*.tar.gz -C /tmp/  
RUN cp /tmp/poliscore*/bin/* /usr/local/bin  
RUN rm -rf /tmp/poliscore*  
  
ADD ./bin /usr/local/bin  
RUN chmod a+x /usr/local/bin/*  
  
# For some reason, docker.io (0.9.1~dfsg1-2) pkg in Ubuntu 14.04 has
permission  
# denied issues when executing /bin/bash from trusted builds. Building locally  
# works fine (strange). Using the upstream docker (0.11.1) pkg from  
# http://get.docker.io/ubuntu works fine also and seems simpler.  
USER polis  
  
VOLUME ["/polis"]  
  
EXPOSE 21426 21427 21430 21431  
WORKDIR /polis  
  
CMD ["polis_oneshot"]  

