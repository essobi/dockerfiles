FROM ubuntu:12.04  
RUN sed -ri "s/archive.ubuntu.com/mirrors.aliyun.com/g" /etc/apt/sources.list  
RUN groupadd -r admin && \  
useradd --create-home --gid admin admin && \  
groupadd -r bae && \  
useradd --create-home --gid bae bae  
  
RUN mkdir -p /home/bae/log && \  
chmod a+rwx /home/bae/log  
# mkdir -p ~/.pip && \  
# echo '[global]' > ~/.pip/pip.conf && \  
# echo 'index-url = https://pypi.tuna.tsinghua.edu.cn/simple' >>
~/.pip/pip.conf && \  
# apt-get update && apt-get install python-pip --no-install-recommends -y && \  
# pip install PyYaml  
COPY ./runtime /home/admin/runtime  
EXPOSE 8080  
VOLUME /home/bae/app  
  
WORKDIR /home/admin/runtime  
  
CMD ["bash", "/home/admin/runtime/run-static.sh", "start"]  
  

