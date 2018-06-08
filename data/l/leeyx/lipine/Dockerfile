FROM alpine:3.4  
  
RUN apk update \  
&& apk add git bash vim musl-dev gcc g++ python3 python3-dev tzdata \  
&& ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime \  
&& echo "Asia/Shanghai" > /etc/timezone \  
&& cp /etc/apk/repositories /etc/apk/repositories.bak \  
&& echo "http://mirrors.aliyun.com/alpine/v3.4/main/" > /etc/apk/repositories
\  
&& apk update \  
&& mkdir -p /root/py/venv \  
&& mkdir /root/.pip/ \  
&& pip3 install -U pip \  
&& pip3 install pbr \  
&& pip3 install virtualenvwrapper \  
&& pip3 install ipython \  
&& pip3 install ipdb \  
&& git clone https://github.com/amix/vimrc.git /root/.vim_runtime \  
&& sh /root/.vim_runtime/install_basic_vimrc.sh  
  
COPY pip.conf /root/.pip/  
  
COPY bashrc /root/.bashrc  

