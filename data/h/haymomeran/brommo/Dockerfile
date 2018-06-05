FROM haymomeran/brommo-prod  
  
# Copy source code  
COPY . /build/  
  
# Install dev modules, build and move app to runtime path  
WORKDIR /build  
  
RUN rm -rf node_modules \  
&& mv /build_node_modules node_modules \  
&& npm set progress=false \  
&& npm install \  
&& npm install --only=dev \  
&& npm run-script build \  
&& mv /build/dist /service \  
&& cp /build/secrets-entrypoint.sh /service \  
&& cp /build/get-secret.js /service  
  
# Install production modules  
WORKDIR /service  
ENV NODE_ENV production  
  
RUN mv /service_node_modules node_modules \  
&& npm set progress=false \  
&& npm install --production \  
&& rm -rf /build /tmp/* /var/tmp/* /root/.npm  
  
# Forward port to container host  
EXPOSE 4040  
# Start service automatically  
CMD ["/bin/sh", "secrets-entrypoint.sh"]  

