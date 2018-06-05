FROM node:8-alpine  
  
ENV ANGULARCLI_VERSION 1.4  
ENV NG_ENV development #default  
  
RUN npm set progress=false && npm config set depth 0 && npm cache clean
--force  
  
# Install Angular CLI  
RUN yarn global add \--no-progress --non-interactive
@angular/cli@${ANGULARCLI_VERSION} && \  
yarn cache clean  
  
# Set yarn as the package manager  
RUN ng set \--global packageManager=yarn  
  
WORKDIR /src  
VOLUME /src/dist  
  
CMD [ "sh", "-c", "ng build --no-delete-output-path --target ${NG_ENV}" ]  

