FROM alpine  
  
RUN apk add -U iproute2  
  
  
ENV INPUT_PORT 80  
ENV TARGET_IP 10.0.0.1  
ENV TARGET_PORT 8080  
  
  
CMD sysctl -w net.ipv4.ip_forward=1 \  
&& iptables -F \  
&& iptables -t nat -F \  
&& iptables -X \  
&& iptables -t nat -A PREROUTING -p tcp --dport $INPUT_PORT -j DNAT --to-
destination $TARGET_IP:$TARGET_PORT \  
&& iptables -t nat -A POSTROUTING -j MASQUERADE \  
&& echo "forwarding $INPUT_PORT to $TARGET_IP:$TARGET_PORT" \  
&& while true; do sleep 1; done  

