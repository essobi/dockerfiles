FROM alpine  
  
MAINTAINER goby<goby@foxmail.com>  
  
# Parameters  
ENV SSL_CA_DIR ""  
ENV SSL_EXPIRY 87600h  
ENV SSL_CA_CN "Kubernetes Netease"  
ENV SSL_COUNTRY "CN"  
ENV SSL_LOCATION "HangZhou"  
ENV SSL_ORGNIZATION "NetEase"  
ENV SSL_ORG_UNIT "Kubernetes"  
ENV SSL_STATE "ZheJiang"  
ENV K8S_APISERVER "127.0.0.1 10.0.0.1 kubernetes kubernetes.default
kubernetes.default.svc kubernetes.default.svc.cluster.local"  
COPY cfssl* /bin/  
COPY run.sh /root/.profile  
  
WORKDIR /opt/cfssl  
VOLUME /opt/cfssl/output  
  
CMD ["sh", "-l"]  

