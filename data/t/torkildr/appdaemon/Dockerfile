FROM acockburn/appdaemon  
MAINTAINER torkildr  
  
RUN pip3 install ics  
  
# hack to support symlinks in static folders  
RUN sed -ri "s/add_static\\((.*)\\)/add_static\\(\1,
follow_symlinks=True\\)/g" /usr/local/lib/python3.6/site-
packages/appdaemon/rundash.py \  
&& ln -s /conf/assets/javascript /usr/local/lib/python3.6/site-
packages/appdaemon/assets/javascript/custom \  
&& ln -s /conf/assets/images /usr/local/lib/python3.6/site-
packages/appdaemon/assets/images/custom  

