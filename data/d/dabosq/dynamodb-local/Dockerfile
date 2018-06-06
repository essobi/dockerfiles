########################################  
#  
# Unofficial image:  
# Amazon AWS DynamoDB local  
#  
# this repo: https://github.com/azza-bazoo/dynamodb-local  
# based on:  
#
http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DynamoDBLocal.html  
#  
########################################  
  
FROM openjdk:9-jre  
  
RUN curl -LO http://dynamodb-local.s3-website-us-
west-2.amazonaws.com/dynamodb_local_latest.tar.gz  
RUN tar -zxf dynamodb_local_latest.tar.gz  
  
EXPOSE 8000  
  
CMD ["java", "-Djava.library.path=./DynamoDBLocal_lib", "-jar",
"DynamoDBLocal.jar", "-sharedDb"]  

