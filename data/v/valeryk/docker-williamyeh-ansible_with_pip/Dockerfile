FROM williamyeh/ansible:ubuntu16.04  
  
RUN apt-get update -y \  
&& apt-get install \--fix-missing \  
&& apt-get install -y python-pip zip \  
&& pip install "pywinrm>=0.2.2" \  
&& apt-get -f -y \--auto-remove remove python-pip \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/*  

