FROM docker.elastic.co/elasticsearch/elasticsearch:6.2.3  
MAINTAINER yangbingdong <yangbingdong1994@gmail.com>  
ARG TZ  
ARG HTTP_PROXY  
ENV TZ=${TZ:-"Asia/Shanghai"} http_proxy=${HTTP_PROXY}
https_proxy=${HTTP_PROXY}  
RUN ./bin/elasticsearch-plugin install https://github.com/medcl/elasticsearch-
analysis-ik/releases/download/v6.2.3/elasticsearch-analysis-ik-6.2.3.zip \  
&& ./bin/elasticsearch-plugin install https://github.com/medcl/elasticsearch-
analysis-pinyin/releases/download/v6.2.3/elasticsearch-analysis-
pinyin-6.2.3.zip \  
&& ln -snf /usr/share/zoneinfo/$TZ /etc/localtime \  
&& echo $TZ > /etc/timezone  
ENV http_proxy=  
ENV https_proxy=  

