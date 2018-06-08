FROM gliderlabs/alpine  
MAINTAINER kost - https://github.com/kost  
  
ADD /scripts /nsrl/  
RUN chmod 755 /nsrl/*  
  
RUN apk --update add python py-pip && apk add gcc libc-dev python-dev >
/tmp/todel && rm -f /var/cache/apk/* && \  
pip install pybloom && \  
/nsrl/shrink_nsrl.sh && \  
apk del --purge `grep "Installing" /tmp/todel | awk '{print $3}'` && \  
rm -rf /tmp/* /root/.cache  
  
WORKDIR /nsrl  
  
ENTRYPOINT ["/nsrl/search.py"]  
  
CMD ["-h"]  

