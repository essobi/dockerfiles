FROM gliderlabs/alpine  
MAINTAINER scorp@3dwars.net  
  
ENV UPDATED_AT 2015-08-17  
RUN apk-install quagga \  
supervisor  
  
ADD supervisord.conf /etc/supervisord.conf  
ADD
https://github.com/SchwarzM/k8s-quagga/releases/download/v0.0.4/k8s-quagga_linux_amd64
/k8s-quagga  
#ADD k8s-quagga /k8s-quagga  
RUN chmod +x /k8s-quagga  
ADD run.sh /run.sh  
RUN chmod +x /run.sh  
  
EXPOSE 179 2601 2604  
CMD ["/run.sh"]  

