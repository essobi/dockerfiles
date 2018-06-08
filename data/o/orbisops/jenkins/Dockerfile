FROM jenkinsci/blueocean:latest  
MAINTAINER Stephen Sullivan <s.sullivan@orbisops.com>  
  
  
ENV CURL_CONNECTION_TIMEOUT=360  
ENV CURL_RETRY_MAX_TIME=120  
ENV CURL_RETRY=6  
# Pipeline plugin  
COPY plugins.txt /usr/share/jenkins/ref/plugins.txt  
RUN (xargs /usr/local/bin/install-plugins.sh <
/usr/share/jenkins/ref/plugins.txt) || \  
(xargs /usr/local/bin/install-plugins.sh < /usr/share/jenkins/ref/plugins.txt)
|| \  
(xargs /usr/local/bin/install-plugins.sh < /usr/share/jenkins/ref/plugins.txt)
|| \  
(xargs /usr/local/bin/install-plugins.sh < /usr/share/jenkins/ref/plugins.txt)
|| \  
(xargs /usr/local/bin/install-plugins.sh < /usr/share/jenkins/ref/plugins.txt)
|| \  
(xargs /usr/local/bin/install-plugins.sh < /usr/share/jenkins/ref/plugins.txt)
|| \  
(xargs /usr/local/bin/install-plugins.sh < /usr/share/jenkins/ref/plugins.txt)
|| \  
(xargs /usr/local/bin/install-plugins.sh < /usr/share/jenkins/ref/plugins.txt)  

