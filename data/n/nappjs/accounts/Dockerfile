FROM nappjs/nappjs  
  
COPY . /code  
  
RUN rm -rf node_modules && \  
npm install --only=production  
  
ENV JWT_CERTS_URL=http://localhost/auth/certs  
  
ENTRYPOINT []  
CMD ["npm","start"]

