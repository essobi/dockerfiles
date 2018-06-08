FROM gcr.io/google_containers/hyperkube-amd64:v1.3.0  
MAINTAINER MidoNet (http://midonet.org)  
  
# MidoNet configuration files  
ADD conf/kuryr.conf /usr/libexec/kubernetes/kubelet-
plugins/net/exec/kuryr.conf  
ADD scripts/run_kubelet.sh /kubelet  
  
# We need to have the CNI driver installed in the kubelet container  
# Clone the kuryr project and install  
RUN apt-get -qy update \  
&& apt-get -qy install git python3 python3-dev build-essential --no-install-
recommends \  
&& curl -s https://bootstrap.pypa.io/get-pip.py | python3 1>/dev/null \  
&& git clone http://github.com/midonet/kuryr /opt/kuryr -b k8s \  
&& cd /opt/kuryr \  
&& pip3 install . \  
&& rm -fr /var/lib/apt/lists/*  
  
#ensure python is defined  
RUN ln -s /usr/bin/python3 /usr/bin/python  
  
ENV MASTER_IP="127.0.0.1"  
ENV ZK_ENDPOINTS="127.0.0.1:2181"  
ENV UUID=""  
ENV PUBLIC_IP=""  
CMD ["/kubelet"]  

