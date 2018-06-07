FROM b0d0nne11/designate-cli  
  
ENV ZONE_ID= \  
RECORDSET_ID=  
  
COPY . /usr/src/app  
  
RUN wget -P /tmp https://github.com/stedolan/jq/releases/download/jq-1.5/jq-
linux64 && mv /tmp/jq-linux64 /usr/local/bin/jq && chmod +x /usr/local/bin/jq  
  
ENTRYPOINT []  
CMD while true; do ./update_record_if_needed.sh; sleep 300; done  

