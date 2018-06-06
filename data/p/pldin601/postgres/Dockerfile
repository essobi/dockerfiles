FROM postgres:9.6  
  
RUN { \  
echo "echo foo"; \  
echo "if [ \"\${POSTGRES_DB_TEST}\" ]; then"; \  
echo " echo Creating test database \"\${POSTGRES_DB}_test\""; \  
echo " createdb --username postgres \"\${POSTGRES_DB}_test\""; \  
echo "fi"; \  
echo ; \  
} > /docker-entrypoint-initdb.d/create_test_database.sh  

