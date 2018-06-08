ARG baseimage=node:8.5.0-alpine  
FROM $baseimage  
  
LABEL com.purrplingcat.name="PurrplingBot"  
LABEL com.purrplingcat.version="1.3.0"  
LABEL com.purrplingcat.vendor="PurrplingCat"  
LABEL com.purrplingcat.email="dev@purrplingcat.com"  
LABEL com.purrplingcat.github="https://github.com/EllenFawkes/PurrplingBot"  
  
ENV DEBUG=0  
ENV APP_DIR="/opt/PurrplingBot"  
ENV APP_CONFIG_DIR="/data/config"  
ENV APP_LOGS="/data/logs/purrplingbot.log"  
ENV PATH=$APP_DIR/bin:$PATH  
  
# Create app place  
RUN mkdir -p $APP_DIR  
WORKDIR $APP_DIR  
# Copy bundle, install main&plugin deps  
COPY . .  
RUN npm install \--only=production && \  
npm run depmod  
  
# Redirect configs to /data/config  
RUN mv config/config.example.yaml extras/config.example.yaml && \  
rm -rf config && \  
ln -s $APP_CONFIG_DIR config  
  
# Redirect logs to /data/logs  
RUN rm -rf purrplingbot.log && \  
ln -s $APP_LOGS purrplingbot.log && \  
ln -s $APP_LOGS /var/log/purrplingbot.log  
  
VOLUME /data/config  
VOLUME /data/logs  
  
# Start PurrplingBot  
CMD ["npm", "start"]  

