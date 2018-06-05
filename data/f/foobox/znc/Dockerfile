FROM alpine:3.7  
EXPOSE 6667  
COPY src /  
RUN znc-setup  
  
USER znc  
ENTRYPOINT ["znc-entrypoint"]  
CMD ["znc", "--foreground", "--datadir=/var/lib/znc"]  
  

