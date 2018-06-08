FROM python:3.4.5-alpine  
MAINTAINER Global Solutions co., ltd.  
LABEL version="0.1.0"  
  
ENV SPHINX_VER=1.4.5 \  
SPHINX_THEMES="sphinxjp.themes.sphinxjp==0.3.1"  
ADD ./entrypoint.sh /sbin/entrypoint.sh  
RUN apk add --no-cache make && \  
pip install sphinx==${SPHINX_VER} ${SPHINX_THEMES} && \  
chmod 755 /sbin/entrypoint.sh  
  
ENTRYPOINT ["/sbin/entrypoint.sh"]  

