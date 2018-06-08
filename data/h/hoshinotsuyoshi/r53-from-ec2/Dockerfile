FROM hoshinotsuyoshi/ruby-aws-sdk:2.1.23  
MAINTAINER hoshinotsuyoshi<guitarpopnot330+docker@gmail.com>  
ADD r53.rb /r53.rb  
ENTRYPOINT ["ruby", "-raws-sdk", "-ropen-uri", "-roptparse", "-rsocket",
"/r53.rb"]  
CMD ["--help"]  

