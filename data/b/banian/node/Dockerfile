FROM node  
# Workdir  
WORKDIR /usr/src/app  
  
# Default CMD  
CMD yarn start  
# Default ENV  
ENV NODE_ENV=production  
  
# Install yarn & setup env  
RUN mkdir -p /usr/src/app && \  
# Install node-prune  
cd /tmp && \  
curl -#L https://github.com/tj/node-prune/releases/download/v1.0.1/node-
prune_1.0.1_linux_amd64.tar.gz | tar -xvzf- && \  
mv -v node-prune /usr/local/bin && rm -rvf * && \  
# Make clean script  
echo "yarn cache clean && node-prune" > /usr/local/bin/node-clean && chmod +x
/usr/local/bin/node-clean  

