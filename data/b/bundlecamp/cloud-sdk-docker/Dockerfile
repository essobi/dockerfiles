FROM ubuntu:15.04  
MAINTAINER admin@bundlecamp.com  
  
VOLUME /var/lib/docker  
  
VOLUME /var/lib/apt/lists  
  
VOLUME ["/.config"]  
  
ADD install_docker.sh /usr/local/bin/install_docker  
  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get update && apt-get install -y -qq --no-install-recommends curl wget
git apt-transport-https ca-certificates curl lxc iptables unzip python
php5-mysql php5-cli php5-cgi openjdk-7-jre-headless openssh-client python-
openssl && apt-get clean  
RUN wget https://dl.google.com/dl/cloudsdk/release/google-cloud-sdk.zip &&
unzip google-cloud-sdk.zip && rm google-cloud-sdk.zip  
ENV CLOUDSDK_PYTHON_SITEPACKAGES 1  
RUN google-cloud-sdk/install.sh --usage-reporting=true \--path-update=true
\--bash-completion=true \--rc-path=/.bashrc --disable-installation-options  
RUN google-cloud-sdk/bin/gcloud --quiet components update pkg-go pkg-python
pkg-java preview alpha beta app  
RUN google-cloud-sdk/bin/gcloud --quiet config set
component_manager/disable_update_check true  
RUN mkdir /.ssh  
ENV PATH /google-cloud-sdk/bin:$PATH  
ENV HOME /  
RUN bash /usr/local/bin/install_docker  
# Install the magic wrapper.  
ADD ./dind/wrapdocker /usr/local/bin/wrapdocker  
  
RUN chmod +x /usr/local/bin/wrapdocker  
  
CMD ["/bin/bash -c 'wrapdocker &' && /bin/bash"]

