FROM pinterb/base:alpine  
  
MAINTAINER Brad Pinter <brad.pinter@gmail.com>  
  
ENV JO_VERSION 1.0  
RUN apk add --no-cache --update-cache ca-certificates make g++ bash sudo
openssh-client && \  
curl -Lo /jo.tar.gz
"https://github.com/jpmens/jo/releases/download/v${JO_VERSION}/jo-${JO_VERSION}.tar.gz"
&& \  
gunzip /jo.tar.gz && tar -xvf /jo.tar && cd /jo-${JO_VERSION} && \  
/jo-${JO_VERSION}/configure && \  
make check && \  
make install && \  
rm -rf /jo-${JO_VERSION} && \  
rm -rf /jo.tar && \  
apk del --purge curl ca-certificates make g++ musl-dev libc-dev && \  
rm -rf /var/cache/apk/*  
  
#ENV PATH /terraform:$PATH  
RUN addgroup dev && \  
adduser -G dev dev -D -h /home/dev && \  
mkdir -p /home/dev/bin /home/dev/lib /home/dev/include /home/dev/.ssh && \  
sed -ri 's/(wheel:x:10:root)/\1,dev/' /etc/group && \  
sed -ri 's/# %wheel ALL=\\(ALL\\) NOPASSWD: ALL/%wheel ALL=\\(ALL\\) NOPASSWD:
ALL/' /etc/sudoers  
  
ENV PATH /home/dev/bin:$PATH  
  
RUN ssh-keygen -t rsa -N '' -f /home/dev/.ssh/dummy_rsa && \  
chown -R dev:dev /home/dev/.ssh  
  
# Create a shared data volume  
# We need to create an empty file, otherwise the volume will  
# belong to root.  
RUN mkdir /data/ /ops/ /state/  
RUN touch /data/.extra /ops/.extra /state/.extra  
RUN chown -R dev:dev /data  
RUN chown -R dev:dev /ops  
RUN chown -R dev:dev /state  
  
## Expose some volumes  
VOLUME ["/data", "/ops", "/state", "/home/dev/.ssh"]  
  
ENV HOME /home/dev  
USER dev  
WORKDIR /data  
  
ENTRYPOINT ["/usr/local/bin/jo"]  
CMD ["--help"]  
#CMD ["/bin/bash"]  

