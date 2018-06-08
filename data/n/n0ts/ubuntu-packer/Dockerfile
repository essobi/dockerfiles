FROM n0ts/ubuntu  
  
MAINTAINER Naoya Nakazawa <naoya.n@gmail.com>  
  
ENV PACKER_VER 1.1.1  
RUN set -x \  
&& curl -L -o /opt/packer-$PACKER_VER.zip \  
https://releases.hashicorp.com/packer/$PACKER_VER/packer_${PACKER_VER}_linux_amd64.zip
\  
&& unzip /opt/packer-$PACKER_VER.zip -d /usr/local/bin/ \  
&& chmod +x /usr/local/bin/packer \  
&& rm -f /opt/packer-$PACKER_VER.zip \  
&& echo "packer version - $(/usr/local/bin/packer --version)"  
  
CMD ["/bin/bash"]  

