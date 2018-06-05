FROM buzzy/build-centos:centos6  
  
RUN curl -O http://public.redjack.com/centos:centos6/buzzy-0.5.1-1.x86_64.rpm
\  
&& sudo yum -y install buzzy-*.rpm \  
&& rm buzzy-*.rpm \  
&& mkdir -p /home/buzzy/.cache/buzzy  

