FROM debian:jessie  
  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
curl \  
python \  
git \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* \  
&& /usr/bin/git config --global http.sslVerify false \  
&& /usr/bin/pip install requests \  
&& /usr/bin/pip install pyyaml \  
&& /usr/bin/pip install gitpython \  
&& /usr/bin/curl -kL https://raw.github.com/pypa/pip/master/contrib/get-pip.py
| python \  
&& mkdir /modules  
  
COPY get_modules.py /usr/local/bin/get_modules.py  
COPY modulelist.yml /etc/modulelist.yml  
  
VOLUME ["/modules"]  
  
ENTRYPOINT ["/usr/local/bin/get_modules.py"]  
  
CMD ["/etc/modulelist.yml", "/modules/" ]  

