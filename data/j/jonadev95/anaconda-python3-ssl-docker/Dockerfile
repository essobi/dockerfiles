FROM ubuntu:16.04  
RUN apt-get update && apt-get install -y bzip2 openssl wget pwgen git
r-recommended  
  
RUN useradd -m -G users conda  
RUN chsh -s /bin/bash conda  
ADD 'https://repo.continuum.io/archive/Anaconda3-4.4.0-Linux-x86_64.sh'
/anaconda.sh  
RUN chown conda:users /anaconda.sh  
  
# jupyter kernels will crash otherwise  
ENV TINI_VERSION v0.6.0  
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini
/usr/bin/tini  
RUN chmod +x /usr/bin/tini  
  
COPY entrypoint.sh /entrypoint.sh  
RUN chmod +x /entrypoint.sh  
  
USER conda  
RUN /bin/bash /anaconda.sh -b  
  
USER root  
RUN rm /anaconda.sh  
USER conda  
  
RUN echo "export PATH=$PATH:/home/conda/anaconda3/bin" >> /home/conda/.bashrc  
  
EXPOSE 8888  
WORKDIR /home/conda/  
ENTRYPOINT ["/usr/bin/tini", "--", "/entrypoint.sh"]  

