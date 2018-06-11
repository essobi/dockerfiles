FROM node  
COPY mock_data/ /VisualizationG5/mock_data/  
COPY express/ /VisualizationG5/express/  
WORKDIR /VisualizationG5/express/  
RUN yarn global add forever  
RUN yarn install  
EXPOSE 3000  
CMD ["npm", "run", "prod-fg"]  

