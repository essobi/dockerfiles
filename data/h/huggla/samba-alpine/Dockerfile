FROM huggla/alpine:20180424  
  
ENV CONFIG_DIR="/etc/samba"  
  
ENV REV_CONFIG_FILE="$CONFIG_DIR/smb.conf" \  
REV_SHARES_DIR="/shares" \  
REV_SHARE_USERS="shareuser" \  
REV_global_smb_passwd_file="$CONFIG_DIR/smbpasswd" \  
REV_global_dns_proxy="no" \  
REV_global_username_map="$CONFIG_DIR/usermap.txt" \  
REV_global_log_file="/var/log/samba/log.%m" \  
REV_global_max_log_size="0" \  
REV_global_syslog="0" \  
REV_global_panic_action="killall smbd" \  
REV_global_server_role="standalone" \  
REV_global_map_to_guest="bad user" \  
REV_global_load_printers="no" \  
REV_global_printing="bsd" \  
REV_global_printcap_name="/dev/null" \  
REV_global_disable_spoolss="yes"  
  
COPY ./bin ${BIN_DIR}  
RUN apk add \--no-cache samba-server \  
&& mv "$REV_CONFIG_FILE" "$REV_CONFIG_FILE.old"  
  
USER sudoer  

