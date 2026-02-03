这是基于箭头音乐精彩点评API开发，查看：https://www.amcfy.xyz/help/comment-api-docs

由于箭头音乐的接口不能发表任何信息，因此基于该接口开发的服务只能查看已有的评论，不能回复或者添加评论，使用服务内置的data_generator.py可以生成测试用的评论，当然如果你能够搞到某q或者某芸的评论api，并且能够解密和匹配，生成comments_data.json，就能够看到它们平台的评论

用法：
1.先在nas或者服务器上构建镜像
sudo docker build -t music-comments-api .
2然后使用docker-compose或者命令
sudo docker run -d -p 8080:8080 --name comments-api music-comments-api 运行
3.生成新的测试数据：curl -X POST "http://nasip:8080/api/comment/generate-test-data"
访问地址：http://nasip:8080
评论数据存储于data/comments_data.json文件中
