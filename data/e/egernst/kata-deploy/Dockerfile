FROM centos/systemd  
ARG KATA_VER=0.2.0  
ARG KATA_URL=https://github.com/kata-
containers/runtime/releases/download/${KATA_VER}  
  
RUN yum install -y wget  
WORKDIR /tmp/kata/  
RUN wget ${KATA_URL}/vmlinuz.container ${KATA_URL}/kata-containers.img  
  
WORKDIR /tmp/kata/bin/  
RUN wget ${KATA_URL}/kata-runtime ${KATA_URL}/kata-proxy ${KATA_URL}/kata-shim  
  
ARG KUBECTL_VER="v1.10.2"  
RUN wget -O /bin/kubectl https://storage.googleapis.com/kubernetes-
release/release/${KUBECTL_VER}/bin/linux/amd64/kubectl && \  
chmod +x /bin/kubectl  
  
COPY bin /tmp/kata/bin  
COPY qemu-artifacts /tmp/kata/share/qemu  
  
COPY configuration.toml /tmp/kata/  
COPY install-kata-crio.sh install-kata-containerd.sh /  

