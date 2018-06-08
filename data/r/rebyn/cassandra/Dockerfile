FROM cassandra:3.11.1  
COPY cassandra-env.sh /etc/cassandra  
COPY stress_test/event_occurrences_full.yaml /  
COPY stress_test/event_occurrences_by_person.yaml /  
COPY stress_test/event_occurrences_id_constraint.yaml /  
COPY stress_test/event_data.yaml /  
COPY stress_test/people_data.yaml /  
  
RUN chmod +x /etc/cassandra/cassandra-env.sh  

