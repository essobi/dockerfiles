FROM python:alpine  
  
VOLUME /log  
EXPOSE 80  
RUN \  
pip install tailon \  
&& apk update \  
&& apk add \  
grep \  
gawk \  
&& echo "#!/bin/sh">/tailon.sh \  
&& echo 'tailon -b 0.0.0.0:80 -t 9999999 -f /log*' >>/tailon.sh \  
&& rm -f /usr/bin/awk /bin/grep \  
&& ln -s /usr/bin/gawk /usr/bin/awk \  
&& ln -s /usr/bin/grep /bin/grep  
  
ENTRYPOINT ["sh", "/tailon.sh"]  
CMD ["*"]  

