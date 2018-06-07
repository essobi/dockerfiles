# See https://github.com/marcus67/docker-graylog  
#  
FROM graylog2/server:2.2.1-1  
COPY assets/move_uid_and_gid.sh /move_uid_and_gid.sh  
COPY assets/entrypoint.sh /entrypoint.sh  
ENTRYPOINT [ "/entrypoint.sh" ]  
CMD [ "graylog" ]  

