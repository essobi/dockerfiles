FROM haproxy:1.6  
COPY haproxy.cfg /usr/local/etc/haproxy/haproxy.cfg  
ENV BACKEND="backend"  
ENV PORT="8080"  
ENV EXPOSE_PORT="80"  
ENV SERVERS=""  
COPY add_servers.sh /add_servers.sh  
  
ENTRYPOINT ["/add_servers.sh"]  
CMD ["haproxy", "-f", "/usr/local/etc/haproxy/haproxy.cfg"]  
  

