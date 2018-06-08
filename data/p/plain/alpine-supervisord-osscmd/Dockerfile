FROM plain/alpine-supervisord-glibc  
  
#RUN wget https://docs-aliyun.cn-hangzhou.oss.aliyun-
inc.com/internal/oss/0.0.4/assets/sdk/OSS_Python_API_20160419.zip?spm=5176.doc32171.2.2.749aGM&file=OSS_Python_API_20160419.zip
\  
# && mv OSS_Python_API_20160419.zip?spm=5176.doc32171.2.2.749aGM
OSS_Python_API_20160419.zip \  
# && unzip OSS_Python_API_20160419.zip && cd OSS_Python_API_20160419  
RUN apk add --no-cache wget  
COPY alioss /alioss  
RUN cd alioss && python setup.py install && chmod +x osscmd && cp osscmd
/usr/bin/  
  
CMD []  
  

