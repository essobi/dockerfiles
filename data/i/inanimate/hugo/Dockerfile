#FROM debian:wheezy  
FROM node:6.3  
ENV NODE_DIR /opt/node  
RUN mkdir ${NODE_DIR}  
WORKDIR ${NODE_DIR}  
COPY package.json ./package.json  
RUN npm install  
RUN echo "export PATH=$PATH:${NODE_DIR}/node_modules/.bin" >> /root/.bashrc  
  
# Install pygments (for syntax highlighting)  
RUN apt-get -qq update \  
&& DEBIAN_FRONTEND=noninteractive apt-get -qq install -y --no-install-
recommends python-pygments \  
&& rm -rf /var/lib/apt/lists/*  
  
# Download and install hugo  
RUN mkdir /opt/hugo  
ENV WORK_DIR /opt/hugo  
ENV HUGO_VERSION 0.20.7  
ENV HUGO_ARCHIVE hugo_${HUGO_VERSION}_Linux-64bit.tar.gz  
ENV HUGO_BINARY hugo  
  
ADD
https://github.com/spf13/hugo/releases/download/v${HUGO_VERSION}/${HUGO_ARCHIVE}
${WORK_DIR}  
RUN tar xzf ${WORK_DIR}/${HUGO_ARCHIVE} -C ${WORK_DIR} \  
&& ln -s ${WORK_DIR}/${HUGO_BINARY} /usr/local/bin/hugo  
  
# Create working directory  
RUN mkdir /usr/share/blog  
WORKDIR /usr/share/blog  
  
# Expose default hugo port  
EXPOSE 1313  
# Automatically build site  
ONBUILD ADD site/ /usr/share/blog  
ONBUILD RUN hugo -d /usr/share/nginx/html/  
  
# By default, serve site  
ENV HUGO_BASE_URL http://localhost:1313  
CMD hugo server -b ${HUGO_BASE_URL}  

