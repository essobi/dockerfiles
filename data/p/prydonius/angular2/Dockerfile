FROM gcr.io/stacksmith-images/ubuntu-buildpack:14.04-r9  
  
RUN bitnami-pkg install node-6.5.0-0 --checksum
52cb7f26dff5661fadb0d3ca50ff4e267b746604a935b3299c3a9383104d0055  
  
ENV PATH=/opt/bitnami/node/bin:/opt/bitnami/python/bin:$PATH \  
NODE_PATH=/opt/bitnami/node/lib/node_modules  
  
RUN npm install -g angular-cli@webpack  
  
COPY rootfs /  
  
USER bitnami  
  
RUN cd ~ && ng new sample --style=scss && \  
# Latest TypeScript version is broken, see https://github.com/angular/angular-
cli/issues/1922#issuecomment-243952252  
cd sample && npm uninstall typescript --save-dev && npm install
typescript@2.0.0 \--save-dev --save-exact && \  
# Latest awesome-typescript-loader is broken, see
https://github.com/angular/angular-cli/issues/1997  
npm uninstall awesome-typescript-loader --save-dev && npm install awesome-
typescript-loader@2.2.1 \--save-dev --save-exact && \  
cd ../ && tar czf sample.tar.gz sample && \  
sudo rm -rf /tmp/npm* sample  
  
WORKDIR /app  
EXPOSE 4200 49152  
ENTRYPOINT ["/app-entrypoint.sh"]  
CMD ["ng", "serve", "-h", "0.0.0.0"]  

