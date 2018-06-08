FROM node:0.12-onbuild  
# URI for API (without trailing /)  
ENV app_url https://api.openphacts.org/latest  
# Get your own key at https://dev.openphacts.org/admin/access_details  
ENV app_id 1c22cbe7  
ENV app_key 167a3a3d8539b5d85280e7178f4e62ab  
  
  
CMD ["node_modules/.bin/jasmine-node", "--captureExceptions", "--config",
"debug", "true", "./test/spec/integration/"]  

