FROM mono:4.4.2.11  
MAINTAINER arielvb  
  
# Fix upgrade problem with mono repository  
RUN echo 'deb http://download.mono-project.com/repo/debian
wheezy/snapshots/4.4.2.11/. main' > /etc/apt/sources.list.d/mono-xamarin.list  
RUN apt-get update && apt-get upgrade -y  
RUN apt-get install monodevelop python3 python3-pip -y  
RUN apt-get install python3-lxml -y  
  
# Upgrade pip  
## Fix pip index url and disable pip version check  
RUN mkdir -p /root/.pip && echo "[global]\nindex-
url=https://pypi.python.org/pypi\ndisable-pip-version-check=true\n" >
/root/.pip/pip.conf  
## Upgrade pip version to the latests supported by Python 3.2  
RUN pip-3.2 install --upgrade "pip==7.1.2"  
## After upgrading pip3-2 is no longer available, create symlink to bring it
back  
RUN ln -s /usr/local/bin/pip3 /usr/local/bin/pip-3.2  
  

