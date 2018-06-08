FROM alpine:3.5  
WORKDIR /tmp  
  
RUN apk add --no-cache wget  
  
RUN mkdir /tmp/frp && \  
mkdir /etc/frp && \  
cd /tmp/frp && \  
ver=$(wget --no-check-certificate -qO-
https://api.github.com/repos/fatedier/frp/releases/latest | grep 'tag_name' |
cut -d\" -f4) && \  
frp_ver="frp_$(echo ${ver} | sed -e 's/^[a-zA-Z]//g')" && \  
wget --no-check-certificate
"https://github.com/fatedier/frp/releases/download/${ver}/${frp_ver}_linux_amd64.tar.gz"
&& \  
tar zxf ${frp_ver}_linux_amd64.tar.gz && \  
mv /tmp/frp/${frp_ver}_linux_amd64/frps /usr/local/bin/frps && \  
chmod +x /usr/local/bin/frps && \  
mv /tmp/frp/${frp_ver}_linux_amd64/frps.ini /etc/frps.ini  
  
CMD ["frps", "-c", "/etc/frp/frps.ini"]

