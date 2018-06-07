# Usage  
#  
# duplicity() {  
# docker run --rm -it \  
# -v "/etc/localtime:/etc/localtime:ro" \  
# -v "/data_to_backup:/data:ro" \  
# -v "$HOME/mydata/cache:/root/.cache" \  
# -e "AWS_ACCESS_KEY_ID=${AWS_ACCESS_KEY_ID}" \  
# -e "AWS_ACCESS_KEY_ID=${AWS_ACCESS_KEY_ID}" \  
# -h duplicity-docker-container \  
# volkerfr/duplicity "$@"  
# }  
FROM alpine  
  
RUN apk --update --no-cache add duplicity ca-certificates  
# Duplicity changed their dependency from lockfile to fasteners  
RUN apk --update --no-cache add py2-pip && pip install fasteners  
  
ENTRYPOINT ["/usr/bin/duplicity"]  

