FROM ubuntu:16.04  
MAINTAINER "Jimmy Song" <http://github.com/jimmysong>  
  
RUN apt update \  
&& DEBIAN_FRONTEND=noninteractive apt install -y openssh-server curl gnupg  
  
# Download Decred  
RUN mkdir /decred  
WORKDIR /decred  
ENV DECRED_VERSION v1.0.3  
ENV DECRED_FILENAME decred-linux-amd64-${DECRED_VERSION}.tar.gz  
ENV MANIFEST manifest-${DECRED_VERSION}.txt  
RUN curl -SLO https://github.com/decred/decred-
binaries/releases/download/${DECRED_VERSION}/${DECRED_FILENAME} \  
&& curl -SLO https://github.com/decred/decred-
binaries/releases/download/${DECRED_VERSION}/${MANIFEST} \  
&& curl -SLO https://github.com/decred/decred-
binaries/releases/download/${DECRED_VERSION}/${MANIFEST}.asc  
  
# Verify and install download  
COPY release-key.asc /decred  
RUN gpg --import release-key.asc \  
&& gpg --verify --trust-model=always ${MANIFEST}.asc \  
&& grep ${DECRED_FILENAME} ${MANIFEST} | sha256sum -c - \  
&& tar -xzf ${DECRED_FILENAME} -C /usr/bin/. --strip-components=1 \  
&& rm ${DECRED_FILENAME} ${MANIFEST} ${MANIFEST}.asc  
  
RUN mkdir /dcrd \  
&& mkdir /dcrwallet  
  
RUN ln -s /dcrd /root/.dcrd \  
&& ln -s /dcrwallet /root/.dcrwallet  
  
RUN mkdir /root/.ssh \  
&& chmod 700 /root/.ssh \  
&& mkdir /var/run/sshd \  
&& perl -p -i -e "s/\\#PasswordAuthentication yes/PasswordAuthentication no/"
/etc/ssh/sshd_config  
  
# Expose SSH port  
EXPOSE 22  
# Expose Peer Port  
EXPOSE 9108  
COPY run.sh /opt  
CMD ["/opt/run.sh"]  

