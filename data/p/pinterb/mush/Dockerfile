FROM pinterb/base:alpine  
  
MAINTAINER Brad Pinter <brad.pinter@gmail.com>  
  
ENV HOME /root  
  
RUN apk add --update \  
make \  
git \  
openssh-client \  
sudo  
  
## Install Mush  
RUN mkdir -p /opt/ && \  
git clone http://github.com/pinterb/mush.git /opt/mush && \  
mkdir -p /usr/local/share/man && \  
cd /opt/mush && make install && \  
apk del make  
  
RUN addgroup dev && \  
adduser -G dev dev -D -h /home/dev && \  
mkdir -p /home/dev/bin /home/dev/lib /home/dev/include /home/dev/.ssh && \  
chown -R dev:dev /home/dev && chown -R dev:dev /home/dev/.ssh && \  
sed -ri 's/(wheel:x:10:root)/\1,dev/' /etc/group && \  
sed -ri 's/# %wheel ALL=\\(ALL\\) NOPASSWD: ALL/%wheel ALL=\\(ALL\\) NOPASSWD:
ALL/' /etc/sudoers  
  
ENV PATH /home/dev/bin:$PATH  
  
# Create a shared data volume  
RUN mkdir /data/ && \  
touch /data/.justignoreme && \  
chown -R dev:dev /data  
  
## Expose some volumes  
VOLUME ["/data", "/home/dev/.ssh"]  
  
ENV HOME /home/dev  
USER dev  
  
WORKDIR /data  
ENTRYPOINT ["/usr/local/bin/mush"]  

