# Docker Definition for ElasticSearch Curator  
FROM python  
MAINTAINER Christian R. Vozar <christian@rogueethic.com>  
  
RUN pip install --quiet elasticsearch-curator  
RUN pip install --quiet requests_aws4auth  
RUN mkdir /actions /config  
WORKDIR /  
  
ENTRYPOINT [ "/usr/local/bin/curator" ]  

