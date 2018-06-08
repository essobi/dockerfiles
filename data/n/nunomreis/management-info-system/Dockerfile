FROM mhart/alpine-node  
  
COPY . /client  
  
ENV PGUSER postgres  
ENV PGHOST localhost  
ENV PGPASSWORD admin  
ENV PGDATABASE postgres  
  
WORKDIR /client/app  
RUN yarn  
  
EXPOSE 3000  
CMD ["yarn","start"]

