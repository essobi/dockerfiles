FROM walkerlee/python3  
MAINTAINER Walker Lee <walkerlee.tw@gmail.com>  
  
RUN apk add --no-cache tini make && \  
pip install --no-cache-dir Sphinx sphinx-rtd-theme sphinx-autobuild
sphinxcontrib-httpdomain  
  
WORKDIR /docs  
  
VOLUME ["/docs"]  
  
EXPOSE 5000  
ENTRYPOINT ["/sbin/tini", "--"]  
  
CMD ["sh", "-c", "/usr/bin/sphinx-autobuild -H 0.0.0.0 -p 5000 -i '.*' -i '*~'
-i '_build/*' -r '\\\d+' /docs /docs/_build/html"]  

