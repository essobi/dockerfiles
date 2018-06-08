FROM alpine:3.4  
RUN apk add --no-cache curl bash python util-linux  
  
RUN curl -L
https://github.com/gliderlabs/sigil/releases/download/v0.4.0/sigil_0.4.0_Linux_x86_64.tgz
\  
| tar -zxC /usr/local/bin  
  
RUN curl https://storage.googleapis.com/kubernetes-
release/release/v1.3.2/bin/linux/amd64/kubectl > /usr/bin/kubectl \  
&& chmod +x /usr/bin/kubectl  
  
RUN cd /tmp \  
&& curl -L https://github.com/ceph/ceph-docker/archive/master.tar.gz | tar
xvzf - ceph-docker-master/examples/kubernetes/generator/ \  
&& mv ceph-docker-master/examples/kubernetes/generator/ /kubernetes-generator
\  
&& rm -rf /tmp/ceph-docker-master  
  
ADD run.sh /run.sh  
RUN chmod +x /run.sh  
  
WORKDIR /kubernetes-generator  
CMD ["/bin/bash","/run.sh"]  

