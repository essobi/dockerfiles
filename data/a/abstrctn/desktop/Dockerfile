FROM ubuntu:xenial  
  
RUN apt-get update  
RUN apt-get install -y git vim wget ruby-full  
  
# Install kubernetes-secret-env  
ENV KUBERNETES_SECRET_ENV_VERSION=0.0.1  
RUN \  
mkdir -p /etc/secret-volume && \  
cd /usr/local/bin && \  
wget -q https://github.com/newsdev/kubernetes-secret-
env/releases/download/$KUBERNETES_SECRET_ENV_VERSION/kubernetes-secret-env &&
\  
chmod +x kubernetes-secret-env  
  
RUN rm -rf /root  
WORKDIR /root  
  
CMD [ "sleep", "infinity" ]  

