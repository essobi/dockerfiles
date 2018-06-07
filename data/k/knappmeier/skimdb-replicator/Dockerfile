FROM couchdb:latest  
  
ADD run-and-replicate.sh replicator.json /  
  
ENTRYPOINT ["/run-and-replicate.sh"]  
CMD [ "couchdb" ]

