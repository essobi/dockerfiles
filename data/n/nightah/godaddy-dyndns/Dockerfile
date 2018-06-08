FROM lsiobase/alpine.python3  
  
# set labels  
LABEL maintainer="Nightah"  
  
# set python to use utf-8 rather than ascii  
ENV PYTHONIOENCODING="UTF-8"  
RUN \  
echo "**** install python dependencies ****" && \  
pip install --no-cache-dir apscheduler requests godaddypy  
  
# copy local files  
COPY root/ /  
  
VOLUME /config  

