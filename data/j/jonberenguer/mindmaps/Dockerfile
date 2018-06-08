FROM centos:7.2.1511  
ENV PATH /opt/node-v6.9.4-linux-x64/bin:$PATH  
  
RUN useradd mindmaps  
  
RUN yum install -y epel-release \  
&& yum install -y git nginx \  
&& line=$(cat /etc/nginx/mime.types | grep -n text/x-component | grep -o
'^[0-9]*') \  
&& sed -i "$line"'i\ text/cache-manifest appcache;' /etc/nginx/mime.types  
  
COPY ./nginx.conf /etc/nginx/  
  
ADD https://nodejs.org/dist/v6.9.4/node-v6.9.4-linux-x64.tar.xz /opt  
  
RUN chown -Rf mindmaps:mindmaps /opt  
  
USER mindmaps  
  
RUN cd /opt \  
&& tar -xvf node-v6.9.4-linux-x64.tar.xz \  
&& rm -f node-v6.9.4-linux-x64.tar.xz \  
&& git clone https://github.com/jonberenguer/mindmaps.git \  
&& cd /opt/mindmaps \  
&& npm install \  
&& jake  
  
USER root  
  
EXPOSE 80  
ENTRYPOINT ["/usr/sbin/nginx"]

