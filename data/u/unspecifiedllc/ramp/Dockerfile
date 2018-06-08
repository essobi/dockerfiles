FROM hashicorp/terraform:light  
COPY /src /ramp  
# ENTRYPOINT ["/ramp/script/entrypoint.sh"]  
ONBUILD ARG CONF_DIR  
ONBUILD COPY ${CONF_DIR} /ramp/conf

