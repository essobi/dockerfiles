FROM alpine:3.7  
ENV DEBUG false  
ENV HTTP true  
ENV HTTPS true  
ENV HTTP_REDIRECT true  
ENV ADMIN true  
  
RUN ln -sf /dev/stdout /var/log/docker.out.log  
RUN ln -sf /dev/stderr /var/log/docker.err.log  
  
COPY entrypoint.sh /  
RUN chmod a+x entrypoint.sh  
  
WORKDIR "/etc/traefik"  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["init"]  

