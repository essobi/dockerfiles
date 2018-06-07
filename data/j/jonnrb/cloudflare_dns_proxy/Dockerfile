from alpine as build  
add https://bin.equinox.io/c/VdrWdbjqyF/cloudflared-stable-linux-amd64.tgz
/cloudflared.tar.gz  
run tar xvf cloudflared.tar.gz  
  
from gcr.io/distroless/base  
copy \--from=build /cloudflared /cloudflared  
env TUNNEL_DNS_ADDRESS "0.0.0.0"  
entrypoint ["/cloudflared", "proxy-dns"]  

