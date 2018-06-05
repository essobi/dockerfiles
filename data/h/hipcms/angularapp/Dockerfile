FROM node  
EXPOSE 8080  
  
RUN mkdir -p /angularapp  
COPY . /angularapp  
  
WORKDIR /angularapp  
  
# install dependencies  
RUN npm install  
RUN npm run postinstall  
  
# build for production  
RUN npm run build:production  
  
# Create hip-config.json, change base URL for subdirectory install, and start
the angular http server  
CMD echo "{ \"authAudience\": \"$AUTH_AUDIENCE\", \"authClientID\":
\"$AUTH_CLIENTID\", \"authDomain\": \"$AUTH_DOMAIN\", \"authRedirectUri\":
\"$AUTH_REDIRECTURL\", \"cmsUrl\": \"$WEBAPI_ADDR\", \"featureToggleUrl\":
\"$FEATURE_TOGGLE_URL\", \"mobileContentApiUrl\": \"$DATASTORE_URL\",
\"achievementApiUrl\": \"$ACHIEVEMENT_URL\", \"userstore\":
\"$USERSTORE_URL\", \"defaultLongitude\": \"$GOOGLE_MAPS_DEFAULT_LONGITUDE\",
\"googleMapsApiKey\": \"$GOOGLE_MAPS_API_KEY\", \"defaultLatitude\":
\"$GOOGLE_MAPS_DEFAULT_LATITUDE\", \"thumbnailApiUrl\": \"$THUMBNAIL_URL\",
\"docsUrl\": \"$DOCS_URL\", \"docsIntegrationUrl\":
\"$DOCS_INTEGRATION_URL\"}" > hip-config.json && sed -i "s/<base
href=\"\/\">/<base href=\"\/$SUB_DIR\/\">/g" index.html && sed -i
"s/e.p=\"\/build\/\",/e.p=\"\/$SUB_DIR\/build\/\",/g" build/vendor.js && npm
run serve  

