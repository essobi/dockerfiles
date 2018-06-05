FROM ricmathie/python_cassandra:python_2.7  
MAINTAINER Richard Mathie "Richard.Mathie@amey.co.uk"  
COPY vendor/github.com/datastax/python-driver/requirements.txt \  
vendor/github.com/datastax/python-driver/test-requirements.txt\  
/benchmarks/  
  
WORKDIR /benchmarks  
  
RUN pip install -r test-requirements.txt  
  
COPY vendor/github.com/datastax/python-driver/benchmarks /benchmarks  
  
ENV CASSANDRA=cassandra \  
KEYSPACE=benchmark_1  
  
CMD ["bash", "-c", "/usr/local/bin/python callback_full_pipeline.py -H
$CASSANDRA -k $KEYSPACE \--protocol-version=4 -m -p --keep-data --column-
type=uuid -c 10 -n 40000"]  

