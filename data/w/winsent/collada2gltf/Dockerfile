FROM python:2.7  
MAINTAINER gneroks@gmail.com  
  
ENV GLTF_VERSION v1.0-draft2  
  
WORKDIR /app  
  
RUN apt-get update && apt-get install -y --no-install-recommends \  
cmake \  
nginx \  
supervisor \  
&& pip install tornado \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Install glTF  
RUN git clone \--recursive https://github.com/KhronosGroup/COLLADA2GLTF.git \  
&& cd COLLADA2GLTF \  
&& git checkout ${GLTF_VERSION} \  
&& cmake . \  
&& make install \  
&& cp ./bin/collada2gltf /usr/local/bin/ \  
&& rm -rf ./glTF/  
  
ADD ./web .  
  
COPY ./docker/nginx.conf /etc/nginx/sites-enabled/default  
COPY ./docker/supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
# forward request and error logs to docker log collector  
RUN ln -sf /dev/stdout /var/log/nginx/access.log \  
&& ln -sf /dev/stderr /var/log/nginx/error.log  
  
EXPOSE 80  
CMD ["supervisord"]  

