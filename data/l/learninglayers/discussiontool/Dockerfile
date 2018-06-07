FROM learninglayers/base  
MAINTAINER Pjotr Savitski <pjotr.savitski [at] tlu.ee>  
  
# Install Nginx  
RUN apt-get update \  
&& apt-get -qqy --no-install-recommends install \  
nginx \  
unzip \  
sed  
  
# Set build directory  
WORKDIR /opt  
  
# Download DiscussionTool distributive  
RUN wget https://github.com/learning-
layers/DiscussionTool/releases/download/v2.6.0/dist.zip \  
&& unzip dist.zip \  
&& rm dist/configurator.sh \  
&& cp -r dist/* /usr/share/nginx/html \  
&& rm *.zip \  
&& rm -r dist  
  
# Provide default port if random port mapping invoked  
EXPOSE 80  
# Do not daemonze  
RUN echo 'daemon off;' >> /etc/nginx/nginx.conf  
  
# Chaange to /root/bin and copy shell files  
WORKDIR /root/bin  
COPY dt-replace-variables.sh dt-replace-variables.sh  
COPY dt-run.sh dt-run.sh  
  
CMD ["bash", "dt-run.sh"]  
  

