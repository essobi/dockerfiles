FROM philippwaller/nodejs:latest  
  
LABEL org.label-schema.schema-version="1.0" \  
org.label-schema.name="Frontail" \  
org.label-schema.description="Frontail"  
  
RUN npm i frontail -g  
  
EXPOSE 9001  
ENTRYPOINT ["frontail"]  
CMD ["--help"]

