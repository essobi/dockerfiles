FROM node:8.9.4  
# Install required packages available from the Debian repo  
# NOTE: output isn't cleaned up so base images can easily run install again
w/o  
# needing to run `apt-get update`  
RUN apt-get update && apt-get install -y \  
python \  
python-dev \  
python-pip \  
rsync \  
shellcheck \  
unzip  
  
# Install pip based packages  
RUN pip install \  
pre-commit \  
awscli==1.14.52  
  
# Install terraform  
RUN curl
https://releases.hashicorp.com/terraform/0.9.6/terraform_0.9.6_linux_amd64.zip
> /root/terraform.zip \  
&& echo "7ec24a5d57da6ef7bdb5a3003791a4368489b32fa93be800655ccef0eceaf1ba
/root/terraform.zip" | sha256sum -c - \  
&& unzip /root/terraform.zip -d /usr/local/bin \  
&& rm /root/terraform.zip  
  
# Install git lfs  
RUN curl https://packagecloud.io/install/repositories/github/git-
lfs/script.deb.sh > /root/git-lfs-installer.sh \  
&& echo "513e12c1614c801ff7c37ce5011116f8b4f36031037f3220625ec005d225f30c
/root/git-lfs-installer.sh" | sha256sum -c - \  
&& chmod a+x /root/git-lfs-installer.sh \  
&& /root/git-lfs-installer.sh \  
&& apt-get install git-lfs \  
&& git lfs install  

