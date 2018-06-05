FROM gcr.io/stacksmith-images/minideb-buildpack:jessie-r9  
  
MAINTAINER Bitnami <containers@bitnami.com>  
  
ENV BITNAMI_APP_NAME=angular \  
BITNAMI_IMAGE_VERSION=2.0.0-r0 \  
PATH=/opt/bitnami/node/bin:/opt/bitnami/python/bin:$PATH \  
NODE_PATH=/opt/bitnami/node/lib/node_modules  
  
# Additional modules required  
RUN bitnami-pkg install node-6.6.0-1 --checksum
36f42bb71b35f95db3bb21d088fbd9438132fb2a7fb4d73b5951732db9a6771e  
  
RUN npm install -g angular-cli@1.0.0-beta.14  
  
COPY rootfs /  
  
USER bitnami  
  
RUN cd ~ && ng new sample --style=scss && \  
tar czf sample.tar.gz sample && \  
sudo rm -rf /tmp/npm* sample  
  
WORKDIR /app  
  
EXPOSE 4200 49152  
ENTRYPOINT ["/app-entrypoint.sh"]  
  
CMD ["ng", "serve", "-h", "0.0.0.0"]  

