FROM yfix/baseimage  
  
MAINTAINER Yuri Vysotskiy (yfix) <yfix.dev@gmail.com>  
  
RUN apt-get update && apt-get install -y software-properties-common \  
&& add-apt-repository -y ppa:builds/sphinxsearch-beta \  
&& apt-get update && apt-get install -y sphinxsearch \  
\  
&& mkdir -p /var/lib/sphinx/data \  
&& mkdir -p /var/log/sphinx \  
&& mkdir -p /var/run/sphinx \  
\  
&& apt-get autoremove -y \  
&& apt-get clean -y \  
&& rm -rf /var/lib/apt/lists/*  
#COPY indexandsearch.sh /etc/my_init.d/indexandsearch.sh  
#COPY searchd.sh /  
#COPY sample.tsv /  
#COPY gosphinx.conf /etc/sphinxsearch/gosphinx.conf  
#COPY container-files /  
#RUN chmod a+x /etc/my_init.d/indexandsearch.sh \  
# && chmod a+x searchd.sh  
# 9312 Sphinx Plain Port  
# 9306 SphinxQL Port  
EXPOSE 9312 9306  

