FROM alpine:3.7  
  
ENV JAIL="none" \  
PID_FILE="/run/varnishd.pid" \  
VARNISH_CONFIG_DIR="/varnishconf" \  
READ_ONLY_PARAMS="cc_command,vcc_allow_inline_c,vmod_path" \  
LISTEN_ADDRESS="" \  
LISTEN_PORT="6081" \  
MANAGEMENT_ADDRESS="localhost" \  
MANAGEMENT_PORT="6082" \  
STORAGE="malloc,100M" \  
DEFAULT_TTL="120" \  
ADDITIONAL_OPTS=""  
  
COPY ./bin/entry.sh /usr/local/bin/entry.sh  
COPY ./varnish-5.0-configuration-templates/default.vcl
"$VARNISH_CONFIG_DIR/default.vcl"  
RUN apk --no-cache add varnish \  
&& mkdir -p "$(dirname '"$PID_FILE"')" \  
&& touch "$PID_FILE" \  
&& chown varnish:varnish "$PID_FILE" \  
&& chmod ugo+x /usr/local/bin/entry.sh  
  
USER varnish  
  
VOLUME "$VARNISH_CONFIG_DIR"  
  
EXPOSE $LISTEN_PORT $MANAGEMENT_PORT  
  
CMD ["entry.sh"]  

