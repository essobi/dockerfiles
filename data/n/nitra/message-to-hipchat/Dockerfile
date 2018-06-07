FROM alpine  
  
RUN apk add --no-cache curl  
  
CMD curl -H "Content-Type: application/json" \  
-H "Authorization: Bearer $TOKEN" \  
-X POST \  
-d "{\"message_format\": \"text\", \"notify\": \"true\", \"message\": \"$MESSAGE\" }" \  
https://nitra.hipchat.com/v2/user/@$USERNAME/message?format=json

