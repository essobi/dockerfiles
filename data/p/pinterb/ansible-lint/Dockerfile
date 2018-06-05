FROM pinterb/base:alpine  
  
MAINTAINER Brad Pinter <brad.pinter@gmail.com>  
  
RUN apk add --update \  
g++ \  
python-dev \  
python \  
sshpass \  
openssh-client \  
sudo \  
py-pip && \  
pip install --upgrade pip && \  
pip install \  
ansible-lint==2.3.1  
## Cleanup  
RUN apk del --purge \  
g++ \  
python-dev \  
make && \  
rm -rf /var/cache/apk/*  
  
RUN addgroup dev && \  
adduser -G dev dev -D -h /home/dev && \  
mkdir -p /home/dev/bin /home/dev/lib /home/dev/include /home/dev/.ssh && \  
chown -R dev:dev /home/dev && chown -R dev:dev /home/dev/.ssh && \  
ssh-keygen -t rsa -N '' -f /home/dev/.ssh/dummy_rsa && \  
sed -ri 's/(wheel:x:10:root)/\1,dev/' /etc/group && \  
sed -ri 's/# %wheel ALL=\\(ALL\\) NOPASSWD: ALL/%wheel ALL=\\(ALL\\) NOPASSWD:
ALL/' /etc/sudoers  
  
ENV PATH /home/dev/bin:$PATH  
  
# Create a shared data volume  
# We need to create an empty file, otherwise the volume will  
# belong to root.  
RUN mkdir /data/ /ops/ /state/ /ansible/ && \  
touch /data/.extra /ops/.extra /state/.extra /ansible/.extra && \  
chown -R dev:dev /data && \  
chown -R dev:dev /ops && \  
chown -R dev:dev /state && \  
chown -R dev:dev /ansible  
  
## Expose some volumes  
VOLUME ["/data", "/ops", "/state", "/ansible", "/home/dev/.ssh"]  
  
ENV HOME /home/dev  
USER dev  
#COPY ansible.cfg $HOME/.ansible.cfg  
WORKDIR /ansible  
  
ENTRYPOINT ["/usr/bin/ansible-lint"]  
CMD ["--help"]  

