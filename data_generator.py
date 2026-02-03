import json
import random
import os
from datetime import datetime, timedelta

def generate_comments_data():
    # 测试数据 - 热门歌曲
    songs = [
        {
            "song_name": "晴天",
            "singer_name": "周杰伦",
            "album_name": "叶惠美",
            "comments": [
                {
                    "nick": "Cheer G",
                    "avatarurl": "https://wx.xxx.cn/mmhead/icTNT8MxQgGcb9lugUn0LWoGdNSVlzm82x7PZRt3Hiba1Y4FfQR06DWuY6tr06coobgvoNpSH7SE4/132",
                    "content": "虽然叫晴天，但整个故事都在下雨",
                    "praiseNum": 234476,
                    "createTime": 1475808377,
                    "commentId": "1001"
                },
                {
                    "nick": "夏雨荷",
                    "avatarurl": "http://y.xxx.cn/music/common/upload/t_celebrity_certification/4150917.jpg",
                    "content": "躺卧在草地独望着晴空，总觉得那年毕业季的夏天蝉鸣额外的聒噪。而老师仿佛一直在讲着同一道题，大家在私底下悄悄地说着话，窗帘的拉卷却总也抵挡不了烈日的阳光。一缕青叶飘落在旁，我睡的很香很香，睡着睡着脸就朝向了你，口袋里五彩的糖果滚落在地上，亮起了一道晴天中的彩虹",
                    "praiseNum": 81788,
                    "createTime": 1627227358,
                    "commentId": "1002"
                },
                {
                    "nick": "音乐爱好者",
                    "avatarurl": "https://randomuser.me/api/portraits/men/32.jpg",
                    "content": "前奏响起，瞬间回到青春时代",
                    "praiseNum": 45231,
                    "createTime": 1583209377,
                    "commentId": "1003"
                }
            ]
        },
        {
            "song_name": "夜曲",
            "singer_name": "周杰伦",
            "album_name": "十一月的萧邦",
            "comments": [
                {
                    "nick": "月光下的诗人",
                    "avatarurl": "https://randomuser.me/api/portraits/women/44.jpg",
                    "content": "为你弹奏萧邦的夜曲，纪念我死去的爱情",
                    "praiseNum": 189234,
                    "createTime": 1495808377,
                    "commentId": "2001"
                },
                {
                    "nick": "古典与现代",
                    "avatarurl": "https://randomuser.me/api/portraits/men/67.jpg",
                    "content": "将古典音乐完美融入流行，周董的才华真的无敌",
                    "praiseNum": 76543,
                    "createTime": 1609227358,
                    "commentId": "2002"
                }
            ]
        },
        {
            "song_name": "Blinding Lights",
            "singer_name": "The Weeknd",
            "album_name": "After Hours",
            "comments": [
                {
                    "nick": "午夜行者",
                    "avatarurl": "https://randomuser.me/api/portraits/men/22.jpg",
                    "content": "This song never gets old! The 80s vibe is amazing.",
                    "praiseNum": 324567,
                    "createTime": 1617227358,
                    "commentId": "3001"
                },
                {
                    "nick": "Synthwave Lover",
                    "avatarurl": "https://randomuser.me/api/portraits/women/33.jpg",
                    "content": "Perfect for driving at night with city lights",
                    "praiseNum": 187654,
                    "createTime": 1628227358,
                    "commentId": "3002"
                }
            ]
        },
        {
            "song_name": "Bohemian Rhapsody",
            "singer_name": "Queen",
            "album_name": "A Night at the Opera",
            "comments": [
                {
                    "nick": "摇滚传奇",
                    "avatarurl": "https://randomuser.me/api/portraits/men/55.jpg",
                    "content": "史上最伟大的摇滚歌曲之一，无法被超越",
                    "praiseNum": 987654,
                    "createTime": 1375808377,
                    "commentId": "4001"
                },
                {
                    "nick": "音乐剧爱好者",
                    "avatarurl": "https://randomuser.me/api/portraits/women/66.jpg",
                    "content": "这不仅仅是一首歌，这是一部微型音乐剧",
                    "praiseNum": 543210,
                    "createTime": 1527227358,
                    "commentId": "4002"
                }
            ]
        }
    ]
    
    # 生成更多随机评论
    all_comments = []
    comment_id = 5000
    
    nicknames = ["音乐达人", "节奏大师", "旋律追寻者", "和弦诗人", "贝斯手小李", 
                 "鼓手小王", "钢琴诗人", "吉他英雄", "声乐爱好者", "编曲师"]
    
    avatars = [f"https://randomuser.me/api/portraits/{gender}/{random.randint(1, 99)}.jpg" 
               for gender in ["men", "women"] for _ in range(50)]
    
    contents = [
        "这首歌的编曲太棒了！",
        "每次听都有新的感受",
        "歌词写得很有深度",
        "主唱的声音太有感染力了",
        "现场版比录音室版还要震撼",
        "十年后再听，依然经典",
        "前奏一响，回忆就涌上心头",
        "这张专辑的巅峰之作",
        "音乐不分国界，好歌传遍世界",
        "强烈推荐给没听过的朋友",
        "The melody is so catchy!",
        "This song brings back so many memories",
        "Perfect for road trips",
        "The production quality is outstanding",
        "Can't stop listening to this"
    ]
    
    for song in songs:
        # 添加预设评论
        for comment in song["comments"]:
            comment["song_name"] = song["song_name"]
            comment["singer_name"] = song["singer_name"]
            comment["album_name"] = song.get("album_name", "")
            all_comments.append(comment)
        
        # 生成随机评论
        for _ in range(random.randint(5, 15)):
            # 随机生成时间戳（最近5年内）
            random_days = random.randint(1, 1825)  # 5年
            random_time = datetime.now() - timedelta(days=random_days)
            timestamp = int(random_time.timestamp())
            
            # 随机生成点赞数
            praise_num = random.randint(100, 50000)
            
            comment = {
                "nick": random.choice(nicknames),
                "avatarurl": random.choice(avatars),
                "content": random.choice(contents),
                "praiseNum": praise_num,
                "createTime": timestamp,
                "commentId": str(comment_id),
                "song_name": song["song_name"],
                "singer_name": song["singer_name"],
                "album_name": song.get("album_name", "")
            }
            
            all_comments.append(comment)
            comment_id += 1
    
    return all_comments

def main():
    data = generate_comments_data()
    
    # 确保data目录存在
    os.makedirs('data', exist_ok=True)
    
    # 保存到文件
    with open('data/comments_data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    print(f"成功生成 {len(data)} 条评论数据")
    print("歌曲统计:")
    
    # 统计各歌曲评论数
    stats = {}
    for comment in data:
        key = f"{comment['song_name']} - {comment['singer_name']}"
        if key not in stats:
            stats[key] = 0
        stats[key] += 1
    
    for song, count in stats.items():
        print(f"  {song}: {count} 条评论")

if __name__ == "__main__":
    main()