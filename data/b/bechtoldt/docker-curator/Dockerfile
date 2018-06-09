FROM alpine:3.4  
  
#TODO remove the sed HACK as soon as
https://github.com/elastic/curator/issues/1064 have been fixed  
  
RUN apk --update add python py-setuptools py-pip && \  
pip install elasticsearch-curator==5.1.2 && \  
apk del py-pip && \  
rm -rf /var/cache/apk/* && \  
sed -i -e 's/3072/1024/g' /usr/lib/python2.7/site-packages/curator/utils.py  
  
ENTRYPOINT ["/usr/bin/curator"]  

