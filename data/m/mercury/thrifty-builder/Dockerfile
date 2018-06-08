FROM python:3.6  
RUN apt-get update \  
&& apt-get -y --no-install-recommends install \  
apt-transport-https \  
ca-certificates \  
curl \  
gnupg2 \  
software-properties-common \  
curl \  
&& apt-get autoremove \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN curl -fsSL https://download.docker.com/linux/$(. /etc/os-release; echo
"$ID")/gpg | apt-key add - \  
&& add-apt-repository \  
"deb [arch=amd64] https://download.docker.com/linux/$(. /etc/os-release; echo
"$ID") \  
$(lsb_release -cs) \  
stable" \  
&& apt-get update \  
&& apt-get -y --no-install-recommends install \  
docker-ce \  
&& apt-get autoremove \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
ENV INSTALL_DIRECTORY=/tmp/thrifty  
RUN mkdir "${INSTALL_DIRECTORY}"  
WORKDIR "${INSTALL_DIRECTORY}"  
ADD . .  
  
RUN python setup.py install  
RUN pip install -r consul-requirements.txt  
  
WORKDIR "/root"  
ENTRYPOINT ["thrifty"]  

