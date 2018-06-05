FROM occitech/cakephp:5-apache  
  
RUN apt-get update \  
&& apt-get install -y locales vim lsof curl \  
&& echo "zh_CN.UTF-8 UTF-8" > /etc/locale.gen \  
&& locale-gen \  
&& apt-get -y autoclean \  
&& apt-get -y clean \  
&& rm -rf /var/cache/apt/archives/* \  
&& rm -rf /var/lib/apt/lists/* \  
&& rm -f /etc/localtime \  
&& ln -s /usr/share/zoneinfo/Asia/Shanghai /etc/localtime  
  
ENV LANG zh_CN.UTF-8  
ENV LC_ALL zh_CN.UTF-8  

