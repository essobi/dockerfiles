FROM nginx  
  
# Install pygments (for syntax highlighting)  
RUN apt-get -qq update \  
&& DEBIAN_FRONTEND=noninteractive apt-get -qq install -y --no-install-
recommends python-pygments \  
&& rm -rf /var/lib/apt/lists/*  
  
# Download and install hugo  
ENV HUGO_VERSION 0.15  
ENV HUGO_BINARY hugo_${HUGO_VERSION}_linux_amd64  
  
ADD
https://github.com/spf13/hugo/releases/download/v${HUGO_VERSION}/${HUGO_BINARY}.tar.gz
/usr/local/  
RUN tar xzf /usr/local/${HUGO_BINARY}.tar.gz -C /usr/local/ \  
&& ln -s /usr/local/${HUGO_BINARY}/${HUGO_BINARY} /usr/local/bin/hugo \  
&& rm /usr/local/${HUGO_BINARY}.tar.gz  
  
# # Create working directory  
RUN mkdir /usr/local/src/hugo  
WORKDIR /usr/local/src/hugo  
  
# # Automatically build site  
ADD site /usr/local/src/hugo/  
RUN hugo \  
&& cp -R /usr/local/src/hugo/public/* /usr/share/nginx/html/  
  
# # Expose default hugo port  
EXPOSE 80  
#  
# # By default, serve site  
# ENV HUGO_BASE_URL http://localhost:1313  
# WORKDIR /usr/share/blog/site  
# CMD hugo server -b ${HUGO_BASE_URL}  
# CMD /bin/bash  

