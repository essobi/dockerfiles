FROM alpine  
  
LABEL
com.ngageoint.seed.manifest="{\"manifestVersion\":\"0.0.1\",\"jobs\":[{\"name\":\"image-
watermark\",\"version\":\"0.1.0\",\"title\":\"Image
Watermarker\",\"description\":\"Processes an input PNG and outputs watermarked
PNG.\",\"authorName\":\"John
Doe\",\"timeout\":30,\"cpus\":1.0,\"mem\":64.0,\"interface\":{\"cmd\":\"\/app\/watermark.py\",\"args\":\"${INPUT_IMAGE}
${JOB_OUTPUT_DIR}\",\"inputData\":{\"files\":[{\"name\":\"INPUT_IMAGE\",\"mediaType\":[\"image\/png\"]}]},\"outputData\":{\"files\":[{\"name\":\"OUTPUT_IMAGE\",\"mediaType\":\"image\/png\",\"pattern\":\"*_watermark.png\"}]}},\"errorMapping\":[{\"code\":1,\"title\":\"Image
Corrupt\",\"description\":\"Image input is not recognized as a valid
PNG.\",\"category\":\"data\"}]}]}"  

