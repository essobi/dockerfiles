FROM alpine:edge  
  
COPY kanban-server.sh /usr/bin/kanban-server  
  
# update/upgrade everything  
RUN apk add --no-cache curl && \  
curl -L -o /usr/bin/kanban
https://github.com/leanlabsio/kanban/releases/download/1.6.2/kanban_x86_64_linux
&& \  
chmod +x /usr/bin/kanban /usr/bin/kanban-server  
  
EXPOSE 80  
CMD ["/usr/bin/kanban-server"]  
  

