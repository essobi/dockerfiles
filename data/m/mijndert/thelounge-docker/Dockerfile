FROM node:8-alpine  
  
ENV NODE_ENV production  
  
ENV THELOUNGE_HOME "/var/opt/thelounge"  
VOLUME "${THELOUNGE_HOME}"  
  
ARG THELOUNGE_VERSION=3.0.0-pre.6  
RUN yarn global add thelounge@${THELOUNGE_VERSION} \--exact \  
&& yarn cache clean  
  
ENV PORT 9000  
EXPOSE ${PORT}  
  
COPY docker-entrypoint.sh /usr/local/bin/docker-entrypoint.sh  
  
ENTRYPOINT ["docker-entrypoint.sh"]  
CMD ["thelounge", "start"]  

