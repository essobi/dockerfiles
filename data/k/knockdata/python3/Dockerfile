FROM debian:stretch  
  
ENV LANG C.UTF-8  
ENV LC_ALL C.UTF-8  
RUN apt-get update \  
&& apt-get install -y bzip2 build-essential curl gcc g++ git grep net-tools
locales sed tar unzip vim wget openssh-server  
  
RUN echo "LC_ALL=\"en_US.UTF-8\"" >> /etc/default/locale  
  
ENV ANACONDA_VERSION 5.0.1  
RUN curl -o ~/anaconda3.sh
https://repo.continuum.io/archive/Anaconda3-${ANACONDA_VERSION}-Linux-x86_64.sh  
  
RUN /bin/bash ~/anaconda3.sh -b -p /opt/conda3 \  
&& rm ~/anaconda3.sh  
  
ENV PATH /opt/conda3/bin:$PATH  
  
RUN conda install -y tensorflow spacy gensim  
  
RUN ssh-keygen -q -N "" -t rsa -f /root/.ssh/id_rsa \  
&& cp /root/.ssh/id_rsa.pub /root/.ssh/authorized_keys \  
&& sed -i "/^[^#]*UsePAM/ s/.*/#&/" /etc/ssh/sshd_config \  
&& echo "UsePAM no" >> /etc/ssh/sshd_config \  
&& echo "Port 2122" >> /etc/ssh/sshd_config \  
&& service ssh start  
  
ADD ssh_config /root/.ssh/config  
RUN chmod 600 /root/.ssh/config  
RUN chown root:root /root/.ssh/config  
  
RUN apt-get clean autoclean \  
&& apt-get autoremove -y --force-yes \  
&& rm -rf /tmp/* \  
&& rm -rf ~/.m2 ~/.npm ~/.cache \  
&& rm -rf /var/lib/{apt,dpkg,cache,log}/  
  
## The default sh has some issue e.g. with source  
## so explicityly change it to bash as the default  
##  
RUN ls -al /bin/sh \  
&& rm /bin/sh \  
&& ln -sf /bin/bash /bin/sh  
  
ADD run.sh /root/run.sh  
  
RUN chmod +x /root/run.sh  
  
CMD ["/root/run.sh"]  

