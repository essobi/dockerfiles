FROM apihackers/pelican  
  
MAINTAINER Eric Lung <longminxiang@163.com>  
  
RUN (apk --update --no-cache add make)  
  
ENV SOURCE_PATH /home/pelican/  
ENV OUTPUT_PATH /output  
  
RUN (echo -e "#!/bin/sh\n\n\  
if [ -d \"\$SOURCE_PATH\" ]; then\n\  
cd \"\$SOURCE_PATH\"\n\  
rm -rf output\n\  
rm -rf $OUTPUT_PATH/*\n\  
make html\n\n\  
cp -r output/* $OUTPUT_PATH\n\  
rm -rf output\n\  
rm -rf __pycache__\n\  
fi\n"\  
>> /run.sh)  
  
CMD ["sh", "/run.sh"]

