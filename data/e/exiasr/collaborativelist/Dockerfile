FROM exiasr/alpine-yarn-nginx:latest  
MAINTAINER Michael(Zichun) Lin <michaellin@ualberta.ca>  
  
# Add package.json and yarn.lock to the container  
ADD package.json yarn.lock /tmp/  
  
# Add local cache to the container  
ADD .yarn-cache.tgz /  
  
# Install packages  
RUN cd /tmp && yarn  
  
# Overwrite nginx conf  
COPY raspberry.conf /etc/nginx/conf.d/default.conf  
  
# Go to Work directory  
WORKDIR /workspace  
  
RUN ln -s /tmp/node_modules  
  
ADD . /workspace  
  
# Prevent environment vairbale being cached  
ARG GOOGLE_CLIENT_ID=1  
ENV GOOGLE_CLIENT_ID ${GOOGLE_CLIENT_ID}  
# install node and yarn  
RUN echo $GOOGLE_CLIENT_ID && yarn run build && \  
cp dist/* /usr/share/nginx/html/  

