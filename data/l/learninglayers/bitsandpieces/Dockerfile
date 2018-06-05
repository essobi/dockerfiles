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
  
# Download BitsAndPieces  
RUN wget https://github.com/learning-layers/BitsAndPieces/archive/v4.5.0.zip \  
&& unzip v*.zip \  
&& cp -r BitsAndPieces-*/* /usr/share/nginx/html \  
&& rm *.zip \  
&& rm -r BitsAndPieces-*  
  
# Provide default port if random port mapping invoked  
EXPOSE 80  
# Do not daemonze  
RUN echo 'daemon off;' >> /etc/nginx/nginx.conf  
  
# Chaange to /root/bin and copy shell files  
WORKDIR /root/bin  
COPY bnp-replace-variables.sh bnp-replace-variables.sh  
COPY bnp-run.sh bnp-run.sh  
  
CMD ["bash", "bnp-run.sh"]  

