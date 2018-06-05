FROM alpine:edge  
RUN sed -i s/cdn/6/ /etc/apk/repositories \  
&& apk add \--update \--progress \  
musl \  
build-base \  
python3 \  
python3-dev \  
bash \  
git \  
&& pip3 install --no-cache-dir --upgrade pip  
  
RUN cd /usr/bin \  
&& ln -sf easy_install-3.5 easy_install \  
&& ln -sf python3 python \  
&& ln -sf pip3 pip  

