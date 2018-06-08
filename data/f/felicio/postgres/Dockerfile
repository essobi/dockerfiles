FROM alpine  
  
RUN apk add --no-cache postgresql  
  
# Copy over server configuration files.  
COPY ["etc/", "/etc/postgresql/"]  
  
# Avoid permissions problems by not setting data directory directly as a
mountpoint.  
# Also represents the only top most directory, where user can store database
clusters.  
VOLUME ["/var/lib/postgresql"]  
  
EXPOSE 5432  
USER postgres  
  
COPY ["docker-entrypoint.sh", "/usr/bin/"]  
  
# Use helper script in order to postpone authentication till runtime.  
ENTRYPOINT ["docker-entrypoint.sh"]  
CMD ["postgres"]  

