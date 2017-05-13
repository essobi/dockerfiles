# vim:set ft=dockerfile:
FROM postgres:9.4
COPY gestalt.sh /docker-entrypoint-initdb.d/gestalt.sh
RUN chmod +x    /docker-entrypoint-initdb.d/gestalt.sh
