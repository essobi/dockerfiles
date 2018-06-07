FROM alpine  
# change source  
RUN echo http://mirrors.ustc.edu.cn/alpine/latest-stable/main/ >
/etc/apk/repositories && \  
echo http://mirrors.ustc.edu.cn/alpine/latest-stable/community/ >>
/etc/apk/repositories && \  
apk --update --no-cache add alpine-sdk python3 python3-dev \  
libffi libffi-dev libressl-dev jpeg-dev zlib-dev  
  
# go into taskalive dir  
WORKDIR /taskalive  
ADD ./setup.py /taskalive  
ADD ./README.md /taskalive  
# update pip and install newest bson  
RUN pip3 install -i https://mirrors.ustc.edu.cn/pypi/web/simple --no-cache-dir
. && \  
pip3 uninstall -y taskalive && rm -r /taskalive && \  
apk del alpine-sdk libffi-dev libressl-dev python3-dev zlib-dev && \  
apk add libressl  

