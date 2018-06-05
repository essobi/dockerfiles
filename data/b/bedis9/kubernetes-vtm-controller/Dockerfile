# docker build -t vtm-controller ~/dockerfiles.local/vtm-controller  
# docker tag vtm-controller:latest myregistry.docker/vtm-controller  
# docker push myregistry.docker/vtm-controller  
FROM ubuntu:16.04  
COPY zinstall.txt /tmp/  
ENV ZEUSFILE=ZeusTM_171_Linux-x86_64.tgz  
ADD svc_discovery_lb.tar.gz /  
COPY installer/ /tmp/  
RUN cd /tmp/ \  
&& apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y
dnsutils curl iproute2 \  
&& if [ ! -f /tmp/$ZEUSFILE ]; then \  
echo "Downloading VTM Installer... Please wait..." ; \  
curl -sSL http://www.badpenguin.co.uk/vadc/$ZEUSFILE > $ZEUSFILE ; \  
fi \  
&& tar -zxvf $ZEUSFILE \  
&& /tmp/Zeus*/zinstall --replay-from=/tmp/zinstall.txt --noninteractive \  
&& rm -rf /tmp/* \  
# controller related information  
&& apt-get install --yes python python-pip \  
&& cd /svc_discovery_lb \  
&& pip install -r ./requirements.txt \  
&& apt-get remove --purge --yes python-pip \  
&& apt-get autoremove --yes \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
COPY zconfig.txt runzeus.sh /usr/local/zeus/  
# ZEUS_EULA must be set to "accept" otherwise the container will do nothing  
ENV ZEUS_EULA=  
# ZEUS_LIC can be used to pass a URL from which the container will download a
license file  
ENV ZEUS_LIC=  
# ZEUS_PASS can be used to set a password. By default a password will be
generated for you  
# ZEUS_PASS=[RANDOM|SIMPLE]: generate a random pass, ZEUS_PASS=STRONG to
employ more symbols.  
# Or ZEUS_PASS=<your password>  
ENV ZEUS_PASS=RANDOM  
# ZEUS_DOM can be used to set a domain and ensure the host has a FQDN.  
ENV ZEUS_DOM=  
# ZEUS_PACKAGES can be used to install additional packages on first run.  
# If you need Java Extensions.... Eg ZEUS_PACKAGES="openjdk-7-jre-headless"  
ENV ZEUS_PACKAGES=  
# ZEUS_DEVMODE can be used to force the vtm to start up in limited development
mode  
ENV ZEUS_DEVMODE=  
# ZEUS_CLUSTER_NAME is used to set the DNS name of an existing member of an
existing cluster  
# we wish to get this new vtm integrated into.  
ENV ZEUS_CLUSTER_NAME=  
# ZEUS Service Director Registratrions  
ENV ZEUS_REGISTER_HOST=  
ENV ZEUS_REGISTER_FP=  
ENV ZEUS_REGISTER_POLICY=  
ENV ZEUS_REGISTER_OWNER=  
ENV ZEUS_REGISTER_SECRET=  
  
# variables for kubernetes controller  
# KUBE_APISERVER is Kubernetes API server URL, including protocol scheme  
ENV KUBE_APISERVER=  
# KUBE_LBNAME is the name of the load-balancer in kubernetes. the controller
use it to  
# watch its configuration  
ENV KUBE_LBNAME=  
# KUBE_LBAPIURL is the vtm API URL, with scheme and a / at the end  
ENV KUBE_LBAPIURL=  
# KUBE_LBAPIPASSWORD is the vtm API password, automatically set by runzeus.sh
to ZEUS_PASS  
ENV KUBE_LBAPIPASSWORD=  
# LBDRIVER is the name of the driver we want to use for this LB  
ENV LBDRIVER=vtm  
  
CMD [ "/usr/local/zeus/runzeus.sh" ]  
EXPOSE 9070 9080 9090 9090/udp 80 443  

