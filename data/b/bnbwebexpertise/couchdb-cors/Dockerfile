FROM couchdb:latest  
  
# Configure CORS  
RUN sed -i -e 's/^enable_cors = false/enable_cors = true/'
/usr/local/etc/couchdb/default.ini && \  
sed -i -e 's/^credentials = false/credentials = true/'
/usr/local/etc/couchdb/default.ini && \  
sed -i -e 's/^;origins = \\*/origins = */' /usr/local/etc/couchdb/default.ini

