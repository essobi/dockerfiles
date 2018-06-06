FROM anapsix/alpine-java  
MAINTAINER ponteineptique <thibault.clerice[@]uni-leipzig.de>  
  
# Install Python  
RUN apk add --no-cache python3 python3-dev gcc linux-headers libxml2
libxml2-dev libxslt libxslt-dev musl musl-dev && \  
python3 -m ensurepip && \  
rm -r /usr/lib/python*/ensurepip && \  
pip3 install --upgrade pip setuptools && \  
rm -r /root/.cache  
  
# Sets up locales to avoid decode issue in python  
ENV LANG C.UTF-8  
RUN pip3 install pbr  
RUN pip3 install HookTest==0.1.0  
  
ADD ./cmds /cmds  
WORKDIR /cmds  
VOLUME /sources  
  
RUN chmod +x tei.sh && chmod +x epidoc.sh  
  
# start supervisor to run our wsgi server  
CMD ["bash"]  

