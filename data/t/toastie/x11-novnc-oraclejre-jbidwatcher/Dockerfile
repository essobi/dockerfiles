#  
# A dockerfile to run JBidwatcher and access it through the browser with
noVNC.  
#  
# BUILD DOCKER: docker build -t toastie/x11-novnc-oraclejre-jbidwatcher .  
# RUN DOCKER: docker run -it -p 8080:8080 toastie/x11-novnc-oraclejre-
jbidwatcher  
# TEST DOCKER: docker exec -it -p 8080:8080 toastie/x11-novnc-oraclejre-
jbidwatcher /bin/bash  
FROM toastie/x11-novnc-oraclejre  
MAINTAINER toastie <user@example.com>  
  
# Expose Port.  
EXPOSE 8080  
# Set correct environment variables.  
ENV HOME /root  
ENV DEBIAN_FRONTEND noninteractive  
ENV LC_ALL C.UTF-8  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US.UTF-8  
ENV TZ Europe/Berlin  
  
  
## Get file name, download and extract JBidWatcher.  
RUN \  
mkdir -p /opt/jbidwatcher \  
&& apt-get install bzip2 \  
&& ver=`wget https://www.jbidwatcher.com/ -O - | grep -o -P
'JBidwatcher\\-.*?.tar.bz2' | head -n1` \  
&& wget -qO- "https://www.jbidwatcher.com/download/"$ver -P /opt/jbidwatcher/
|\  
tar -jx --strip-components=1 -C /opt/jbidwatcher/  
  
## Auto-connect  
RUN sed -i 's/<body>/<body
onload="document.getElementById(\x27noVNC_connect_button\x27).click();">/g' \  
/opt/noVNC/vnc.html  
  
# Configure & run supervisor  
COPY jbidwatcher.conf /etc/supervisor/conf.d/jbidwatcher.conf  
CMD ["/usr/bin/supervisord"]  

