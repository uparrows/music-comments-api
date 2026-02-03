from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import os
import time
from datetime import datetime

app = Flask(__name__)
CORS(app)

def load_comments():
    data_file = 'data/comments_data.json'
    if os.path.exists(data_file):
        with open(data_file, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

def save_comments(comments):
    data_file = 'data/comments_data.json'
    os.makedirs(os.path.dirname(data_file), exist_ok=True)
    with open(data_file, 'w', encoding='utf-8') as f:
        json.dump(comments, f, ensure_ascii=False, indent=2)

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy", "timestamp": int(time.time())}), 200

@app.route('/api/comment/list', methods=['GET'])
def get_comments():
    try:
        song_name = request.args.get('song_name')
        singer_name = request.args.get('singer_name')
        album_name = request.args.get('album_name')
        
        if not song_name or not singer_name:
            return jsonify({
                "code": 400,
                "msg": "缺少必选参数：song_name 和 singer_name 必须提供",
                "body": []
            }), 400
        
        start = int(request.args.get('start', 0))
        limit = int(request.args.get('limit', 100))
        lang = request.args.get('lang', 'en-US')
        order_by = request.args.get('order_by', 'new')
        
        all_comments = load_comments()
        
        filtered_comments = []
        for comment in all_comments:
            if (comment['song_name'].lower() == song_name.lower() and 
                comment['singer_name'].lower() == singer_name.lower()):
                if album_name:
                    if comment.get('album_name', '').lower() == album_name.lower():
                        filtered_comments.append(comment)
                else:
                    filtered_comments.append(comment)
        
        if order_by == 'hot':
            filtered_comments.sort(key=lambda x: x['praiseNum'], reverse=True)
        else:
            filtered_comments.sort(key=lambda x: x['createTime'], reverse=True)
        
        paginated_comments = filtered_comments[start:start + limit]
        
        response_body = []
        for comment in paginated_comments:
            response_body.append({
                "nick": comment["nick"],
                "avatarurl": comment["avatarurl"],
                "content": comment["content"],
                "praiseNum": comment["praiseNum"],
                "createTime": comment["createTime"],
                "commentId": comment["commentId"]
            })
        
        return jsonify({
            "code": 200,
            "msg": "获取成功",
            "body": response_body
        }), 200
        
    except Exception as e:
        return jsonify({
            "code": 500,
            "msg": f"服务器错误: {str(e)}",
            "body": []
        }), 500

# 添加测试数据端点（仅开发使用）
@app.route('/api/comment/generate-test-data', methods=['POST'])
def generate_test_data():
    try:
        from data_generator import generate_comments_data
        comments = generate_comments_data()
        save_comments(comments)
        return jsonify({
            "code": 200,
            "msg": f"成功生成 {len(comments)} 条测试数据",
            "body": []
        }), 200
    except Exception as e:
        return jsonify({
            "code": 500,
            "msg": f"生成测试数据失败: {str(e)}",
            "body": []
        }), 500

@app.route('/api/stats', methods=['GET'])
def get_stats():
    comments = load_comments()
    
    song_stats = {}
    for comment in comments:
        key = f"{comment['song_name']} - {comment['singer_name']}"
        if key not in song_stats:
            song_stats[key] = 0
        song_stats[key] += 1
    
    return jsonify({
        "code": 200,
        "msg": "统计信息",
        "body": {
            "total_comments": len(comments),
            "unique_songs": len(song_stats),
            "song_stats": song_stats
        }
    }), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=False)