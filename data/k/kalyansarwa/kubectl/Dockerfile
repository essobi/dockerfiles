FROM tenstartups/alpine  
  
# environment variable to be used with kubectl config  
ENV SERVER=localhost  
  
RUN wget -O /usr/local/bin/dumb-init https://github.com/Yelp/dumb-
init/releases/download/v1.2.1/dumb-init_1.2.1_amd64  
RUN curl -LO https://storage.googleapis.com/kubernetes-release/release/$(curl
-s https://storage.googleapis.com/kubernetes-
release/release/stable.txt)/bin/linux/amd64/kubectl  
  
ADD setkube.sh /setkube.sh  
ADD setkube.sh /root/.bash_profile  
ADD setkube.sh /root/.bashrc  
  
RUN mv ./kubectl /usr/local/bin/kubectl  
RUN chmod a+x /usr/local/bin/kubectl /usr/local/bin/dumb-init /setkube.sh
/root/.bash_profile /root/.bashrc  
  
RUN apk --no-cache del ca-certificates openssl  
  
# ENTRYPOINT ["/usr/bin/curl"]  
# ENTRYPOINT ["/usr/local/bin/dumb-init","--","/usr/local/bin/docker-
entrypoint.sh"]  
CMD ["/bin/bash"]  

