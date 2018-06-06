FROM izone/amdgpu:17.40.2712  
MAINTAINER Leonardo Loures <luvres@hotmail.com>  
  
ENV \  
POOL="s.comining.io" \  
PORT="9999" \  
USER="A8bW7QQtc8igRn5EEZgoBBD.1uvr3z" \  
USERPASS="x"  
RUN \  
cd \  
&& apt-get update \  
&& apt-get --no-install-recommends install -y libcurl3  
  
ADD Claymore_v11.8.tar.gz /opt/  
  
CMD /opt/Claymore_v11.8/ethdcrminer64 -epool $POOL:$PORT -ewal $USER -epsw
$USERPASS -allpools 1  

